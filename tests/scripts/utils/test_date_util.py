from datetime import date

from scripts.utils.date_util import date_range


def test_date_range():
    results = list(date_range("2022-01-01", "2022-01-03"))
    assert results == [date(2022, 1, 1), date(2022, 1, 2)]
