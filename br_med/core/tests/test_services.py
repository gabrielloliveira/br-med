import json

import httpretty
import pytest
from django.conf import settings

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


@pytest.fixture
def rates():
    return {
        "date": "2020-04-03",
        "base": "USD",
        "rates": {
            "EUR": 0.9272137227630969,
            "USD": 1,
            "JPY": 108.57672693555864,
            "BGN": 1.813444598980065,
            "CZK": 25.534538711172928,
            "DKK": 6.925266573945294,
            "GBP": 0.8145572554473806,
            "HUF": 338.5720908669448,
            "PLN": 4.243393602225313,
            "RON": 4.479091330551692,
            "SEK": 10.154844691701436,
            "CHF": 0.9779323133982383,
            "ISK": 144.36717663421416,
            "NOK": 10.443022716736207,
            "HRK": 7.074640704682429,
            "RUB": 76.78025034770515,
            "TRY": 6.703384330088085,
            "AUD": 1.6693555864626797,
            "BRL": 5.275197032916087,
            "CAD": 1.4185442744552619,
            "CNY": 7.09095966620306,
            "HKD": 7.753824756606399,
            "IDR": 16614.44598980065,
            "ILS": 3.6408901251738524,
            "INR": 76.23180343069076,
            "KRW": 1235.8089939731108,
            "MXN": 24.614742698191932,
            "MYR": 4.358460825220213,
            "NZD": 1.7082058414464534,
            "PHP": 50.815948076031525,
            "SGD": 1.4361613351877607,
            "THB": 33.009735744089014,
            "ZAR": 18.789244320815946,
        },
    }


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


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_rates(rates):
    """
    Service should be return dict that contain rates
    """

    base_url = settings.VAT_URL.rstrip("/")
    currencies_url = base_url + "/rates"
    httpretty.register_uri(httpretty.GET, currencies_url, body=json.dumps(rates))

    service = VATService()
    response = service.rates()

    assert response == rates
