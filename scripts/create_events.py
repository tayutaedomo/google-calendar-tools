import argparse
import datetime

from utils.api import insert_event 


def main():
    args = parse_args()

    calendar_id = args.calendar
    summary = args.title

    for date_ in date_range(args.from_date, args.to_date):
        start_datetime_str = create_datetime_str(date_, args.start_oclock)
        end_datetime_str = create_datetime_str(date_, args.end_oclock)

        params = {
            'calendarId': calendar_id,
            'body': {
                'summary': summary,
                'start': {
                    'dateTime': start_datetime_str,
                },
                'end': {
                    'dateTime': end_datetime_str,
                },
            }
        }

        response = insert_event(params)
        print(response)


def parse_args():
    parser = argparse.ArgumentParser(description='Fetch events and export to csv.')
    parser.add_argument('calendar', type=str, help='Target calendar id of Google Calendar')
    parser.add_argument('from_date', type=str, help='Start date for events (e.g. 2021-01-01)')
    parser.add_argument('to_date', type=str, help='End date for events (e.g. 2021-01-02')
    parser.add_argument('start_oclock', type=str, help="Start o'clock for events (e.g. 09:00:00)")
    parser.add_argument('end_oclock', type=str, help="End o'clock for events (e.g. 09:30:00)")
    parser.add_argument('title', type=str, help="Event title")

    return parser.parse_args()


def date_range(from_date_str, to_date_str):
    start_date = datetime.date(*[int(i) for i in from_date_str.split('-')])
    end_date = datetime.date(*[int(i) for i in to_date_str.split('-')])
    for ordinal in range(start_date.toordinal(), end_date.toordinal()):
        yield datetime.date.fromordinal(ordinal)


def create_datetime_str(date_, oclock_str):
    return f"{date_}T{oclock_str}+0900"


if __name__ == '__main__':
    main()
