# isort:skip_file
from __future__ import annotations

import argparse
import logging
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__)))

from utils.events import CreateEventsInput, create_events


def main() -> None:
    args = parse_args()
    setup_logger()

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


def parse_args():
    parser = argparse.ArgumentParser(description="Fetch events and export to csv.")
    parser.add_argument("calendar_id", type=str, help="Google Calendar ID")
    parser.add_argument("summary", type=str, help="Event Summary")
    parser.add_argument("from_date", type=str, help="Start date (e.g. 2021-01-01)")
    parser.add_argument("to_date", type=str, help="End date for (e.g. 2021-01-02")
    parser.add_argument("start_time", type=str, help="Start time (e.g. 09:00:00)")
    parser.add_argument("end_time", type=str, help="End time (e.g. 09:30:00)")
    parser.add_argument("--weekday", action="store_true", help="Weekday only")

    return parser.parse_args()


def setup_logger(level=logging.INFO) -> None:
    logging.basicConfig(level=logging.INFO)
    log_format = "%(levelname)s %(asctime)s - %(message)s"
    logging.basicConfig(stream=sys.stdout, format=log_format, level=level)


if __name__ == "__main__":
    main()
