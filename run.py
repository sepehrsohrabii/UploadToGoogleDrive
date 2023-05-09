from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request

import os


# Define the scope of access
SCOPES = ['https://www.googleapis.com/auth/drive']

# Define the path to the credentials JSON file
CLIENT_SECRET_FILE = 'client_secret_472889574093-r2vstebsjghkepuc8k3joioim7rp8t6e.apps.googleusercontent.com.json'

# Define the ID of the folder where you want to upload the file
FOLDER_ID = '1Ux3jOFPWAPMgX-G_EXG1tHBcektAnZbu'

def upload_file_to_drive(file_path):
    # Authenticate and build the Drive API client
    creds = None
    
    # Check if the credentials file exists and is valid
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        
    # If the credentials are not valid or don't exist, refresh them or authenticate the user
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRET_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    
    # Build the Drive API client
    drive_service = build('drive', 'v3', credentials=creds)

    # Upload the file to Google Drive
    try:
        file_metadata = {'name': os.path.basename(file_path),
                         'parents': [FOLDER_ID]}
        media = MediaFileUpload(file_path,
                                mimetype='application/vnd.ms-excel')
        file = drive_service.files().create(body=file_metadata,
                                            media_body=media,
                                            fields='id').execute()
        print(F'File ID: {file.get("id")}')

    # Handle any HTTP errors that occur during the upload
    except HttpError as error:
        print(F'An error occurred: {error}')
        file = None

    # Return the uploaded file's ID
    return file

file_path = 'orders_test.xlsx'
upload_file_to_drive(file_path)