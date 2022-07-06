import json
from unittest import mock

import httpretty
import pytest
from django.conf import settings
from django.test import override_settings

from br_med.core.services import VATService


@pytest.fixture
def currencies():
    return {
        "EUR": {"name": "Euro", "symbol": "€"},
        "USD": {"name": "US Dollar", "symbol": "$"},
        "JPY": {"name": "Japanese Yen", "symbol": "¥"},
        "BGN": {"name": "Bulgarian Lev", "symbol": "BGN"},
        "CZK": {"name": "Czech Koruna", "symbol": "CZK"},
        "DKK": {"name": "Danish Krone", "symbol": "DKK"},
        "GBP": {"name": "British Pound", "symbol": "£"},
        "HUF": {"name": "Hungarian Forint", "symbol": "HUF"},
        "PLN": {"name": "Polish Zloty", "symbol": "PLN"},
        "RON": {"name": "Romanian Leu", "symbol": "RON"},
        "SEK": {"name": "Swedish Krona", "symbol": "SEK"},
        "CHF": {"name": "Swiss Franc", "symbol": "CHF"},
        "ISK": {"name": "Icelandic Króna", "symbol": "ISK"},
        "NOK": {"name": "Norwegian Krone", "symbol": "NOK"},
        "HRK": {"name": "Croatian Kuna", "symbol": "HRK"},
        "RUB": {"name": "Russian Ruble", "symbol": "RUB"},
        "TRY": {"name": "Turkish Lira", "symbol": "TRY"},
        "AUD": {"name": "Australian Dollar", "symbol": "A$"},
        "BRL": {"name": "Brazilian Real", "symbol": "R$"},
        "CAD": {"name": "Canadian Dollar", "symbol": "CA$"},
        "CNY": {"name": "Chinese Yuan", "symbol": "CN¥"},
        "HKD": {"name": "Hong Kong Dollar", "symbol": "HK$"},
        "IDR": {"name": "Indonesian Rupiah", "symbol": "IDR"},
        "ILS": {"name": "Israeli New Shekel", "symbol": "₪"},
        "INR": {"name": "Indian Rupee", "symbol": "₹"},
        "KRW": {"name": "South Korean Won", "symbol": "₩"},
        "MXN": {"name": "Mexican Peso", "symbol": "MX$"},
        "MYR": {"name": "Malaysian Ringgit", "symbol": "MYR"},
        "NZD": {"name": "New Zealand Dollar", "symbol": "NZ$"},
        "PHP": {"name": "Philippine Piso", "symbol": "PHP"},
        "SGD": {"name": "Singapore Dollar", "symbol": "SGD"},
        "THB": {"name": "Thai Baht", "symbol": "THB"},
        "ZAR": {"name": "South African Rand", "symbol": "ZAR"},
    }


@override_settings(VAT_URL="https://fake.com")
@httpretty.activate(verbose=True, allow_net_connect=False)
def test_currencies(currencies):
    """
    Service should be return dict that contain currencies
    """

    base_url = settings.VAT_URL.rstrip("/")
    currencies_url = base_url + "/currencies"
    httpretty.register_uri(httpretty.GET, currencies_url, body=json.dumps(currencies))

    service = VATService()
    response = service.currencies()

    assert response == currencies


@override_settings(VAT_URL="https://fake.com")
@httpretty.activate(verbose=True, allow_net_connect=False)
def test_rates(rates):
    """
    Service should be return dict that contain rates
    """

    base_url = settings.VAT_URL.rstrip("/")
    rates_url = base_url + "/rates"
    httpretty.register_uri(httpretty.GET, rates_url, body=json.dumps(rates))

    service = VATService()
    response = service.rates()

    assert response == rates


@mock.patch.object(VATService, "get", autospec=True)
def test_service_rates_has_base_in_usd(mock_get):
    """
    Service should pass in query params base=USD
    """

    service = VATService()
    service.rates()

    assert mock_get.called
    assert "base" in mock_get.call_args.kwargs["query_params"]
    assert mock_get.call_args.kwargs["query_params"]["base"] == "USD"
