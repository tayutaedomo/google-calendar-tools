from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from logging import getLogger
from typing import Any

from utils.date_util import date_range
from utils.google_api import fetch_events, insert_event

logger = getLogger(__name__)


class Events:
    def __init__(self):
        self.items = []

    def fetch(self, params):
        loop_count = 1
        self.items = []

        params["pageToken"] = None

        while True:
            response = fetch_events(params)

            if response and response.get("items"):
                self.items.extend(response.get("items"))

            page_token = response.get("nextPageToken")

            if not page_token:
                params["pageToken"] = page_token
                break

            if loop_count > 20:
                break

            if loop_count % 5 == 0:
                logger.info(f"Fetching. items:{len(self.items)}, loop:{loop_count}")

            loop_count += 1

        logger.info(f"Fetched. items:{len(self.items)}, loop:{loop_count}")

        return self.items

    def to_csv(self, filename):
        for obj in self.items:
            item = EventItem(obj)

            if item.is_cancelled():
                continue

            csv_line = '"{}","{}","{}","{}","{}"'.format(
                item.get_summary(),
                "1" if item.is_all_day() else "0",
                item.get_start(),
                item.get_end(),
                item.get_total_minitues(),
            )

            with open(filename, "a") as f:
                f.write(csv_line + "\n")


class EventItem:
    def __init__(self, item):
        self.item = item

    def is_cancelled(self) -> bool:
        return self.item.get("status") == "cancelled"

    def get_summary(self):
        return self.item.get("summary")

    def has_start(self):
        return self.item.get("start") is not None

    def get_start(self):
        d = self.get_start_date()
        if d != "":
            return d

        return self.get_start_datetime()

    def get_start_date(self):
        start = self.item.get("start")

        if not start:
            return ""

        d = start.get("date")
        if d:
            return d

        return ""

    def get_start_datetime(self):
        start = self.item.get("start")

        if not start:
            return ""

        dt = start.get("dateTime")
        if dt:
            return dt

        return ""

    def is_all_day(self):
        return self.get_start_date() != ""

    def get_end(self):
        d = self.get_end_date()
        if d != "":
            return d

        return self.get_end_datetime()

    def get_end_date(self):
        end = self.item.get("end")

        if not end:
            return ""

        d = end.get("date")
        if d:
            return d

        return ""

    def get_end_datetime(self):
        end = self.item.get("end")

        if not end:
            return ""

        dt = end.get("dateTime")
        if dt:
            return dt

        return ""

    def get_total_minitues(self):
        if not self.has_start() or self.is_all_day():
            return 0

        start = datetime.fromisoformat(self.get_start_datetime())
        end = datetime.fromisoformat(self.get_end_datetime())
        return (end - start).total_seconds() / 60


@dataclass
class CreateEventsInput:
    calendar_id: str
    summary: str
    from_date: str
    to_date: str
    start_time: str
    end_time: str
    weekday: bool = False


def create_events(input_: CreateEventsInput) -> list[Any]:
    def create_datetime_str(date_, time_str):
        return f"{date_}T{time_str}+0900"

    responses = []

    for date_ in date_range(input_.from_date, input_.to_date):
        start_datetime_str = create_datetime_str(date_, input_.start_time)
        end_datetime_str = create_datetime_str(date_, input_.end_time)

        if input_.weekday and date_.isoweekday() in {6, 7}:
            continue

        params = {
            "calendarId": input_.calendar_id,
            "body": {
                "summary": input_.summary,
                "start": {
                    "dateTime": start_datetime_str,
                },
                "end": {
                    "dateTime": end_datetime_str,
                },
            },
        }
        response = insert_event(params)
        responses.append(response)

    return responses
