import pytest
from model_bakery import baker


@pytest.fixture
def currency(db):
    return baker.make("core.Currency", acronym="usd")


def test_currency_acronym_is_uppercase(currency):
    """Currency acronym should be in uppercase"""
    first_acronym = currency.acronym
    currency.acronym = "brl"
    currency.save(update_fields=["acronym"])
    currency.refresh_from_db()
    assert first_acronym == "USD"
    assert currency.acronym == "BRL"
