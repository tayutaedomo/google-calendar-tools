from datetime import date


def date_range(from_date_str, to_date_str):
    start_date = date(*[int(i) for i in from_date_str.split("-")])
    end_date = date(*[int(i) for i in to_date_str.split("-")])
    for ordinal in range(start_date.toordinal(), end_date.toordinal()):
        yield date.fromordinal(ordinal)
