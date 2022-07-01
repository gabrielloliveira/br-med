from datetime import date

from br_med.core.utils import range_dates, get_period_from_request


def test_range_dates():
    """range dates with period 2020-01-01 - 2020-01-05 should return an list with 5 elements"""
    start_at = date(2020, 1, 1)
    end_at = date(2020, 1, 5)
    list_dates = range_dates(start_at=start_at, end_at=end_at)
    expected_dates = [
        date(2020, 1, 1),
        date(2020, 1, 2),
        date(2020, 1, 3),
        date(2020, 1, 4),
        date(2020, 1, 5),
    ]
    assert len(list_dates) == 5
    assert list_dates == expected_dates


def test_get_period_from_request():
    """should return typle of dates"""
    request = {
        "start_at": "2020-01-01",
        "end_at": "2020-01-01",
    }
    expected = (date(2020, 1, 1), date(2020, 1, 1))
    result = get_period_from_request(request)

    assert expected == result


def test_get_period_from_request_with_no_request():
    """if start_at in request, should date today"""
    request = dict()
    expected = (date.today(), date.today())
    result = get_period_from_request(request)

    assert expected == result
