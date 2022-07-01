from datetime import date, timedelta


def range_dates(start_at: date, end_at: date):
    """
    Helper function to return a range dates in period

    :param start_at: date from init
    :param end_at: date from finish
    :return: list with dates in range
    """
    list_dates = [start_at]
    while start_at < end_at:
        start_at = start_at + timedelta(days=1)
        list_dates.append(start_at)
    return list_dates
