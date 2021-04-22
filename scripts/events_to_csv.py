import os
import sys
from datetime import datetime

sys.path.append(os.path.join(os.path.dirname(__file__)))

from utils.events import Events


def main():
  if len(sys.argv) < 2:
    print('Calendar ID is required.')
    return

  if len(sys.argv) < 4:
    print('Start date and End date are required.')
    print('Format: 2021-01-01T00:00:00+0900')
    return

  events = Events()

  params = {
      'calendarId': sys.argv[1],
      'timeMin': sys.argv[2],
      'timeMax': sys.argv[3],
  }

  if len(sys.argv) > 4:
    params['q'] = sys.argv[4]

  events.fetch(params)

  filename = datetime.now().strftime('%y%m%d_%H%M%S.csv')
  events.to_csv(filename)


if __name__ == '__main__':
    main()
