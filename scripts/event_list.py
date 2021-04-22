import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__)))

# from utils.api import get_calendar_service
from utils.api import fetch_events


def main():
  if len(sys.argv) < 2:
    print('Calendar ID is required.')
    return

  if len(sys.argv) < 4:
    print('Start date and End date are required.')
    print('Format: 2021-01-01T00:00:00Z')
    return

  calendar_id = sys.argv[1]
  start_date = sys.argv[2]
  end_date = sys.argv[3]
  print(calendar_id, start_date, end_date)

  # service = get_calendar_service()
  # events = service.events().list(calendarId=calendar_id, maxResults=10, timeMin=start_date).execute()

  params = {
      'calendarId': calendar_id,
      'timeMin': start_date,
      'timeMax': end_date,
      'maxResults': 10,
  }
  events = fetch_events(params)

  for (idx, item) in enumerate(events['items'], 1):
    # print(item)
    print(idx, item['summary'], item['start'], item['end'])


if __name__ == '__main__':
    main()
