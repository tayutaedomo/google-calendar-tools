import os
import sys
from datetime import datetime, timedelta, timezone
import calendar

sys.path.append(os.path.join(os.path.dirname(__file__)))

from utils.api import get_calendar_service


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

  service = get_calendar_service()

  events = service.events().list(calendarId=calendar_id, maxResults=10, timeMin=start_date).execute()
  for item in events['items']:
    # print(item)
    print(item['summary'], item['start'], item['end'])


# def get_dates():
#   start_date = None
#   end_date = None

#   if len(sys.argv) > 2:
#     try:
#       start_date = sys.argv[2]
#       end_date = sys.argv[3]
#     except Exception:
#       start_date, end_date = get_default_dates()
#   else:
#     start_date, end_date = get_default_dates()

#   return (start_date, end_date)


# def get_default_dates():
#   today = datetime.utcnow().date()

#   # One day
#   # start_date = datetime(today.year, today.month, today.day, tzinfo=timezone.utc)
#   # end_date = start_date + timedelta(1)

#   # One month
#   _, days = calendar.monthrange(today.year, today.month)
#   start_date = datetime(today.year, today.month, 1, tzinfo=timezone.utc)
#   end_date = datetime(today.year, today.month, days, tzinfo=timezone.utc) + timedelta(1)

#   return (start_date, end_date)


if __name__ == '__main__':
    main()
