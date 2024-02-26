# https://developers.google.com/drive/api/v3/reference/files/list
# The needed import for service account credentials:
import os
from oauth2client.service_account import ServiceAccountCredentials
from apiclient.discovery import build
from apiclient.http import MediaFileUpload

scope = ['https://www.googleapis.com/auth/drive']

# Parsing JSON credentials for a service account:
credentials = ServiceAccountCredentials.from_json_keyfile_name('client_cred.json', scope)

service = build('drive', 'v3', credentials=credentials)

# Replace 'YOUR_FOLDER_ID' with the actual ID of the parent folder in Google Drive:
parent_folder_id = 'YOUR_FOLDER_ID'

# delete the old dump in the google drive
results = service.files().list(
    pageSize=5, fields="nextPageToken, files(id, name, mimeType, size, parents, modifiedTime)").execute()

items = results.get('files', [])
for item in items:
    if item['name'] == 'my-dump.xml':
        print('I will try to delete this file:')
        print(u'{0} ({1})'.format(item['name'], item['id']))
        del_response = service.files().delete(fileId=item['id']).execute()
        print('del_response.body:')
        print(del_response)

# upload file to server
file_metadata = { 'name' : 'my-dump.xml','parents': [parent_folder_id]}
media = MediaFileUpload('my-dump.xml',mimetype='text/xml')
file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()

#delete dump
os.remove("./my-dump.xml")
