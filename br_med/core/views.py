from django.contrib import messages
from django.shortcuts import render

from br_med.core.enums import CurrencyEnum
from br_med.core.exceptions import PeriodIsTooLargeException
from br_med.core.models import Quote
from br_med.core.utils import get_period_from_request, range_dates


def index(request):
    try:
        start_at, end_at = get_period_from_request(request.GET)
    except PeriodIsTooLargeException:
        messages.error(request, "O Período é muito grande para ser pesquisado.")
        return render(request, "core/index.html")
    context = {
        "period": {"start_at": start_at, "end_at": end_at},
        "range_dates": range_dates(start_at, end_at),
        "results": [],
    }
    available_currencies = CurrencyEnum.choices
    for currency in available_currencies:
        key = currency[0]
        if key == "USD":
            continue
        quotes = (
            Quote.objects.filter(
                date__range=[start_at, end_at],
                currency=key,
            )
            .order_by("-date")
            .values_list("value", flat=True)
        )
        data = {
            "key": key,
            "quotes": quotes,
        }
        context["results"].append(data)
    return render(request, "core/index.html", context=context)
