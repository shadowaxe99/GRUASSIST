# Source: ai_executive_assistant.py

import datetime
import pytz
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


class AIExecutiveAssistant:
    def __init__(self):
        self.creds = None
        self.service = None
        self.init_service()

    def init_service(self):
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', ['https://www.googleapis.com/auth/calendar', 'https://www.googleapis.com/auth/gmail.send'])
                self.creds = flow.run_local_server(port=0)
            with open('token.pickle', 'wb') as token:
                pickle.dump(self.creds, token)
        self.service = build('calendar', 'v3', credentials=self.creds)
        self.gmail_service = build('gmail', 'v1', credentials=self.creds)

    def schedule_meeting(self, start_time, end_time, summary, description, attendees):
        event = {
            'summary': summary,
            'description': description,
            'start': {
                'dateTime': start_time,
                'timeZone': 'America/Los_Angeles',
            },
            'end': {
                'dateTime': end_time,
                'timeZone': 'America/Los_Angeles',
            },
            'attendees': [{'email': attendee} for attendee in attendees],
            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'email', 'minutes': 24 * 60},
                    {'method': 'popup', 'minutes': 10},
                ],
            },
        }
        event = self.service.events().insert(calendarId='primary', body=event).execute()
        print(f'Event created: {event.get('htmlLink')}')

    def send_email(self, to, subject, message):
        message = MIMEMultipart()
        message['to'] = to
        message['subject'] = subject
        message.attach(MIMEText(message, 'plain'))
        raw_message = base64.urlsafe_b64encode(message.as_string().encode('utf-8')).decode('utf-8')
        message = self.gmail_service.users().messages().send(userId='me', body={'raw': raw_message}).execute()
        print(f'Message Id: {message['id']}')

    def set_reminder(self, title, notes, due):
        from googleapiclient.discovery import build
        from google.oauth2.credentials import Credentials
        from google_auth_oauthlib.flow import InstalledAppFlow
        from google.auth.transport.requests import Request
        import os.path
        import pickle

        # If modifying these SCOPES, delete the file token.pickle.
        SCOPES = ['https://www.googleapis.com/auth/tasks']

        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('tasks', 'v1', credentials=creds)

        task = {
            'title': title,
            'notes': notes,
            'due': due
        }
        result = service.tasks().insert(tasklist='@default', body=task).execute()
        print('Task created: %s' % result['id'])

    def get_weather(self):
        pass

    def manage_todo_list(self):
        pass

    def query_database(self):
        pass

    def read_file(self):
        pass

    def write_file(self):
        pass