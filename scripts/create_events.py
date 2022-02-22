from __future__ import annotations

import argparse
import datetime
from dataclasses import dataclass
from typing import Any

from utils.api import insert_event


@dataclass
class CreateEventsInput:
    calendar_id: str
    summary: str
    from_date: str
    to_date: str
    start_time: str
    end_time: str
    weekday: bool = False


def main():
    args = parse_args()
    input_ = CreateEventsInput(
        calendar_id=args.calendar_id,
        summary=args.summary,
        from_date=args.from_date,
        to_date=args.to_date,
        start_time=args.start_time,
        end_time=args.end_time,
        weekday=args.weekday,
    )

    responses = create_events(input_)
    print(f"Created. count:{len(responses)}")


def create_events(input_: CreateEventsInput) -> list[Any]:
    responses = []

    for date_ in date_range(input_.from_date, input_.to_date):
        start_datetime_str = create_datetime_str(date_, input_.start_time)
        end_datetime_str = create_datetime_str(date_, input_.end_time)

        if input_.weekday and date_.isoweekday() in {6, 7}:
            continue

        params = {
            'calendarId': input_.calendar_id,
            'body': {
                'summary': input_.summary,
                'start': {
                    'dateTime': start_datetime_str,
                },
                'end': {
                    'dateTime': end_datetime_str,
                },
            }
        }
        response = insert_event(params)
        responses.append(response)

    return responses


def parse_args():
    parser = argparse.ArgumentParser(description='Fetch events and export to csv.')
    parser.add_argument('calendar_id', type=str, help='Target calendar id of Google Calendar')
    parser.add_argument('summary', type=str, help="Event Summary")
    parser.add_argument('from_date', type=str, help='Start date (e.g. 2021-01-01)')
    parser.add_argument('to_date', type=str, help='End date for (e.g. 2021-01-02')
    parser.add_argument('start_time', type=str, help="Start time (e.g. 09:00:00)")
    parser.add_argument('end_time', type=str, help="End time (e.g. 09:30:00)")
    parser.add_argument('--weekday', action='store_true', help='Weekday only')

    return parser.parse_args()


def date_range(from_date_str, to_date_str):
    start_date = datetime.date(*[int(i) for i in from_date_str.split('-')])
    end_date = datetime.date(*[int(i) for i in to_date_str.split('-')])
    for ordinal in range(start_date.toordinal(), end_date.toordinal()):
        yield datetime.date.fromordinal(ordinal)


def create_datetime_str(date_, time_str):
    return f"{date_}T{time_str}+0900"


if __name__ == '__main__':
    main()
