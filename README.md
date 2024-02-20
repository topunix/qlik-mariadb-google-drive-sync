# MariaDB to Qlik Sense Data Synchronization via Google Drive

## Overview

This repository contains a Python script designed to facilitate data synchronization from a MariaDB database to Qlik Sense using Google Drive as an intermediary storage. Due to Qlik Sense's limitation in connecting directly to MariaDB, this script provides a workaround by creating a database dump in XML format, uploading it to Google Drive, and allowing Qlik Sense to read from the file stored in Google Drive.

## Workflow

The script follows a three-step workflow:

1. **Delete Old Dump:**
   - Checks for an existing file named 'alfred-dump.xml' on Google Drive.
   - If found, deletes the old dump file.

2. **Upload New Dump:**
   - Uploads a new version of the 'alfred-dump.xml' file to Google Drive using the Google Drive API.

3. **Delete Local Dump:**
   - Deletes the local copy of the 'alfred-dump.xml' file from the machine.

## Requirements

- **Service Account Credentials:**
  - A JSON key file for a service account with appropriate permissions to access Google Drive. This file should be named 'client_cred.json' and placed in the same directory as the script.

- **Python Libraries:**
  - Ensure the following Python libraries are installed:
    - `oauth2client`
    - `google-api-python-client`

  You can install them using the following command:
  ```bash
  pip install oauth2client google-api-python-client
