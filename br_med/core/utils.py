import datetime
from datetime import date, timedelta

from br_med.core.exceptions import PeriodIsTooLargeException

MAX_QTD_DAYS_FROM_PERIOD = 5


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


def get_period_from_request(data: dict) -> tuple:
    today = str(datetime.date.today())
    start_at = data.get("start_at", today)
    end_at = data.get("end_at", today)

    start_at = datetime.datetime.strptime(start_at, "%Y-%m-%d").date()
    end_at = datetime.datetime.strptime(end_at, "%Y-%m-%d").date()

    if (end_at - start_at).days > MAX_QTD_DAYS_FROM_PERIOD:
        raise PeriodIsTooLargeException()

    return start_at, end_at
