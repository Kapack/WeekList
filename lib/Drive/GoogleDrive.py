# Token
from __future__ import print_function
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# Download
import io
from googleapiclient.http import MediaIoBaseDownload

# os
from definitions import ROOT_DIR
import os.path
import webbrowser

class GoogleDrive:
	def __init__(self):
		self.SCOPES = ['https://www.googleapis.com/auth/drive']

	def token(self):
		# Root path
		path = ROOT_DIR + '/lib/Drive/auth/'
		creds = None
		

		# The file token.json stores the user's access and refresh tokens, and is
		# created automatically when the authorization flow completes for the first
		# time.

		if os.path.exists(path + 'token.json'):
			# Below code from Drive document, dosn't work... It works be generate a new token every time. Therefor we delete it.
			os.remove(path + 'token.json')
			#creds = Credentials.from_authorized_user_file(path + 'token.json', self.SCOPES)
		
		# If there are no (valid) credentials available, let the user log in.
		if not creds or not creds.valid:
			if creds and creds.expired and creds.refresh_token:
				creds.refresh(Request())
			else:
				flow = InstalledAppFlow.from_client_secrets_file(path + 'credentials.json', self.SCOPES)
				creds = flow.run_local_server(port=0)
			
			# Save the credentials for the next run
			with open(path + 'token.json', 'w') as token:
				token.write(creds.to_json())

			service = build('drive', 'v3', credentials=creds)

			return service


	def downloadFile(self, serviceToken, weekNumber, file_id):				
		# Create path if not exists
		path = ROOT_DIR + '/' + weekNumber + '/'		
		if not os.path.exists(path):
			os.makedirs(path)

		# Getting metaData
		metaData = serviceToken.files().get(fileId=file_id).execute()
		fileName = metaData['name']
		# Getting the file
		request = serviceToken.files().get_media(fileId=file_id)
		fh = io.FileIO(path + fileName, mode='wb')
		downloader = MediaIoBaseDownload(fh, request)
		done = False
		while done is False:
			status, done = downloader.next_chunk()
			print("Download List from Drive %d%%." % int(status.progress() * 100))
			
			# Returns the filename
			return fileName	
	
	def openChecklistFolder(self):
		# Open in Browser
		url = 'https://drive.google.com/drive/folders/0B5Y507CtwfIwMWNTN21QZkpwMFk?resourcekey=0-AT_5j3otEM_Z30kH5mBcZw'
		webbrowser.open(url, new=0)	