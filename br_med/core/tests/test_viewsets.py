import json
from unittest import mock

import httpretty
from django.conf import settings
from django.test import override_settings
from rest_framework import status
from rest_framework.reverse import reverse

from br_med.core.enums import CurrencyEnum
from br_med.core.models import Quote


class TestQuoteListView:
    @override_settings(VAT_URL="https://fake.com")
    @httpretty.activate(verbose=True, allow_net_connect=False)
    def test_list_with_no_data(self, db, rates, client):
        """If not data in Quote, then call service and save data"""

        base_url = settings.VAT_URL.rstrip("/")
        currencies_url = base_url + "/rates"
        httpretty.register_uri(httpretty.GET, currencies_url, body=json.dumps(rates))

        response = client.get(reverse("core:api-quote-list"))

        assert Quote.objects.count() > 0
        assert len(response.data["results"]) == len(CurrencyEnum.choices)
        assert response.status_code == status.HTTP_200_OK

    @mock.patch("br_med.core.services.VATService", autospec=True)
    def test_list_with_previous_data(self, mock_service, db, quote, client):
        """if data in db, then api should not call service"""

        response = client.get(reverse("core:api-quote-list"))

        assert Quote.objects.count() == 1
        assert response.status_code == status.HTTP_200_OK
        assert not mock_service.called
