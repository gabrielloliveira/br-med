from django.db.models import TextChoices


class CurrencyEnum(TextChoices):
    USD = "USD"
    BRL = "BRL"
    EUR = "EUR"
    JPY = "JPY"
