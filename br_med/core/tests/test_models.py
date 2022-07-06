import json
from datetime import date

import httpretty
from django.conf import settings
from django.test import override_settings

from br_med.core.models import Quote


@override_settings(VAT_URL="https://fake.com")
@httpretty.activate(verbose=True, allow_net_connect=False)
def test_search_in_service_filter(db, rates):
    """
    Service should be return dict that contain rates
    """

    base_url = settings.VAT_URL.rstrip("/")
    currencies_url = base_url + "/rates"
    httpretty.register_uri(httpretty.GET, currencies_url, body=json.dumps(rates))

    count_first_query = Quote.objects.count()
    Quote.objects.filter_by_period(start_at=date(2020, 1, 1), end_at=date(2020, 1, 1))

    assert count_first_query == 0
    assert Quote.objects.count() == 4
