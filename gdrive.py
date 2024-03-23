import os
import re
import json
import requests
import urllib.parse
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload  # Import MediaIoBaseDownload
from parcv import parcv  # Import your resume parsing library

# Function to authenticate with Google Drive API
def authenticate():
    credentials_file = 'credentials.json'  # Path to your credentials JSON file
    SCOPES = ['https://www.googleapis.com/auth/drive']

    flow = InstalledAppFlow.from_client_secrets_file(credentials_file, SCOPES)
    credentials = flow.run_local_server(port=0)

    # Save credentials for future use
    with open('token.json', 'w') as token:
        token.write(credentials.to_json())

    return credentials

# Function to list files in a Google Drive folder
def list_files_in_folder(service, folder_id):
    results = service.files().list(q=f"'{folder_id}' in parents and trashed=false",
                                   fields="files(id, name)").execute()
    files = results.get('files', [])
    return files

# Function to download a file from Google Drive
def download_file(service, file_id, destination):
    request = service.files().get_media(fileId=file_id)
    with open(destination, 'wb') as file:
        downloader = MediaIoBaseDownload(file, request)
        done = False
        while not done:
            status, done = downloader.next_chunk()

# Authenticate with Google Drive API
credentials = authenticate()

# Build the Google Drive service
service = build('drive', 'v3', credentials=credentials)

# Prompt user to drop the link to the folder containing resumes
folder_link = input("Enter the link to the folder containing resumes: ")

# Extract folder ID from the link
folder_id = urllib.parse.urlparse(folder_link).path.split('/')[-1]

# List files in the folder
files = list_files_in_folder(service, folder_id)

# Process each resume
for file in files:
    # Output the filename
    print(file['name'])
