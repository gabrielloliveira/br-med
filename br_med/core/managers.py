from datetime import date

from django.db import models

from br_med.core.enums import CurrencyEnum
from br_med.core.services import VATService
from br_med.core.utils import range_dates


class QuoteQuerySet(models.QuerySet):
    def filter_by_period(self, start_at: date, end_at: date):
        list_dates = range_dates(start_at=start_at, end_at=end_at)
        dates_in_db = self.filter(date__range=[start_at, end_at]).values_list("date", flat=True)

        dates_to_search_in_service = list(set(list_dates) - set(dates_in_db))
        self.model.objects.search_quote_in_service(dates_to_search_in_service)

        return self.filter(date__range=[start_at, end_at])


class QuoteManager(models.Manager):
    def get_queryset(self):
        return QuoteQuerySet(self.model, using=self.db)

    def filter_by_period(self, start_at: date, end_at: date):
        return self.get_queryset().filter_by_period(start_at, end_at)

    def search_quote_in_service(self, list_dates: list = None):
        list_dates = list_dates if list_dates else []

        valid_currencies = CurrencyEnum.values
        bulk_create_list = []

        service = VATService()

        for period in list_dates:
            rates = service.rates(period)

            for currency, value in rates["rates"].items():
                if currency not in valid_currencies:
                    continue

                instance = self.model(date=period, currency=currency, value=value)
                bulk_create_list.append(instance)

        self.bulk_create(bulk_create_list)
