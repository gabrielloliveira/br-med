from django.contrib import admin

from br_med.core.models import Currency, Quote
from django.utils.translation import gettext_lazy as _


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ["acronym"]
    search_fields = ["acronym", "name", "symbol"]


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ["date", "acronym", "value"]
    autocomplete_fields = ["currency"]

    def acronym(self, obj):
        return obj.currency.acronym

    acronym.short_description = _("Moeda")
