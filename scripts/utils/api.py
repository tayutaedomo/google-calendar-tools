from __future__ import annotations

import os.path
import pickle
from typing import Any

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = [
    'https://www.googleapis.com/auth/calendar.readonly',
    'https://www.googleapis.com/auth/calendar.events',
]

CREDENTIALS_PATH = os.path.join(os.path.dirname(
    __file__), '..', '..', 'etc', 'google-cloud', 'credentials.json')


def get_calendar_service(scopes=None):
    scopes = scopes or SCOPES
    creds = None

    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, scopes)
            creds = flow.run_local_server()

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('calendar', 'v3', credentials=creds)


def fetch_events(params):
    service = get_calendar_service()
    return service.events().list(**params).execute()


def insert_event(params) -> Any:
    service = get_calendar_service()
    return service.events().insert(**params).execute()
