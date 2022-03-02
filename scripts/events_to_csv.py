# isort:skip_file
from __future__ import annotations

import argparse
import logging
import os
import sys
from datetime import datetime

sys.path.append(os.path.join(os.path.dirname(__file__)))

from utils.events import Events


def main():
    args = parse_args()
    setup_logger()

    params = {
        "calendarId": args.calendar,
        "timeMin": args.min,
        "timeMax": args.max,
        "maxResults": 2500,
    }

    if args.keyword:
        params["q"] = args.keyword

    events = Events()
    events.fetch(params)

    filename = datetime.now().strftime("%y%m%d_%H%M%S.csv")
    events.to_csv(filename)


def parse_args():
    parser = argparse.ArgumentParser(description="Fetch events and export to csv.")
    parser.add_argument(
        "calendar", type=str, help="Target calendar id of Google Calendar"
    )
    parser.add_argument(
        "min", type=str, help="Min datetime for Query (e.g. 2021-01-01T00:00:00+0900)"
    )
    parser.add_argument(
        "max", type=str, help="Max datetime for Query (e.g. 2021-01-01T00:00:00+0900)"
    )
    parser.add_argument("--keyword", type=str, help="Query keyword")

    return parser.parse_args()


def setup_logger(level=logging.INFO) -> None:
    logging.basicConfig(level=logging.INFO)
    log_format = "%(levelname)s %(asctime)s - %(message)s"
    logging.basicConfig(stream=sys.stdout, format=log_format, level=level)


if __name__ == "__main__":
    main()
