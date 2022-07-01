from django.shortcuts import render

from br_med.core.enums import CurrencyEnum
from br_med.core.utils import get_period_from_request


def index(request):
    start_at, end_at = get_period_from_request(request.GET)
    context = {
        "currencies": CurrencyEnum.choices,
        "start_at": start_at,
        "end_at": end_at,
    }
    return render(request, "core/index.html", context=context)
