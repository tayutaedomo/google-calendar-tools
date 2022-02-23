from __future__ import annotations

from unittest.mock import Mock, patch

from utils.events import CreateEventsInput, create_events


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
