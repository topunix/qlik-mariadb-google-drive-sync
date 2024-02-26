# MariaDB to Qlik Sense Data Synchronization via Google Drive

## Overview

This repository contains a Python script designed to facilitate data synchronization from a MariaDB database to Qlik Sense using Google Drive as an intermediary storage. Due to Qlik Sense's limitation in connecting directly to MariaDB, this script provides a workaround by creating a database dump in XML format, uploading it to Google Drive, and allowing Qlik Sense to read from the file stored in Google Drive.

**UPDATE: December 2023.** All ODBC data sources, except ServiceNow, are now supported with Qlik Data Gateway - Direct Access.

## Workflow

The script follows a three-step workflow:

1. **Delete Old Database Dump:**
   - Checks for an existing file named 'my-dump.xml' on Google Drive.
   - If found, deletes the old dump file.

2. **Upload New Database Dump:**
   - Uploads a new version of the 'my-dump.xml' file to Google Drive using the Google Drive API.

3. **Delete Local Database Dump:**
   - Deletes the local copy of the 'my-dump.xml' file from the machine.

## Requirements

- **Service Account Credentials:**
  - A JSON key file for a service account with appropriate permissions to access Google Drive. This file should be named 'client_cred.json' and placed in the same directory as the script.

- **Parent Folder ID:**
  - Replace the placeholder in the script with the actual ID of the parent folder in Google Drive where you want to store the database dump. You can obtain the folder ID by right-clicking on the folder in Google Drive and selecting "Share." The ID will be in the URL as `https://drive.google.com/drive/folders/YOUR_FOLDER_ID`.

- **Python Libraries:**
  - Ensure the following Python libraries are installed:
    - `oauth2client`
    - `google-api-python-client`

  You can install them using the following command:
  ```bash
  pip install oauth2client google-api-python-client
