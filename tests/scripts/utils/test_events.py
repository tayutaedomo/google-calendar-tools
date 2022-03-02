from __future__ import annotations

from typing import Any
from unittest.mock import Mock, patch

from utils.events import CreateEventsInput, Events, create_events


@patch("utils.events.insert_event", return_value={})
def test_create_events(mock_insert_event: Mock) -> None:
    input_ = CreateEventsInput(
        calendar_id="primary",
        summary="summary",
        from_date="2022-02-25",
        to_date="2022-02-27",
        start_time="09:00:00",
        end_time="09:00:00",
        weekday=False,
    )

    responses = create_events(input_)
    assert len(responses) == 2
    mock_insert_event.assert_called()


@patch("utils.events.insert_event", return_value={})
def test_create_events_with_weekday(mock_insert_event: Mock) -> None:
    input_ = CreateEventsInput(
        calendar_id="primary",
        summary="summary",
        from_date="2022-02-25",
        to_date="2022-02-27",
        start_time="09:00:00",
        end_time="09:00:00",
        weekday=True,
    )

    responses = create_events(input_)
    assert len(responses) == 1
    mock_insert_event.assert_called_once()


EXPECTED_RESPONSE: dict[str, Any] = {
    "items": [
        {
            "status": "confirmed",
            "summary": "item 1",
            "start": {
                "dateTime": "2022-02-01T09:00:00+09:00",
                "timeZone": "Asia/Tokyo",
            },
            "end": {
                "dateTime": "2022-02-01T09:30:00+09:00",
                "timeZone": "Asia/Tokyo",
            },
        },
        {
            "status": "confirmed",
            "summary": "item 2",
            "start": {
                "dateTime": "2022-02-01T09:30:00+09:00",
                "timeZone": "Asia/Tokyo",
            },
            "end": {
                "dateTime": "2022-02-01T09:45:00+09:00",
                "timeZone": "Asia/Tokyo",
            },
        },
        {
            "status": "cancelled",
            "summary": "item cancelled",
            "start": {
                "dateTime": "2022-02-01T10:00:00+09:00",
                "timeZone": "Asia/Tokyo",
            },
            "end": {
                "dateTime": "2022-02-01T10:30:00+09:00",
                "timeZone": "Asia/Tokyo",
            },
        },
    ]
}


@patch("utils.events.fetch_events", return_value=EXPECTED_RESPONSE)
def test_events_fetch(mock_fetch_events: Mock) -> None:
    events = Events()
    params = {
        "calendarId": "primary",
        "timeMin": "2022-02-01T00:00:00+0900",
        "timeMax": "2022-02-02T00:00:00+0900",
    }
    events.fetch(params)
    assert len(events.items) == 3

    expected_item: dict[str, Any] = EXPECTED_RESPONSE["items"][0]
    item: dict = events.items[0]
    assert item["summary"] == expected_item["summary"]
