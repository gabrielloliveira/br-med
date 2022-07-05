from rest_framework import generics
from rest_framework.response import Response

from br_med.core.models import Quote
from br_med.core.serializers import QuoteByPeriodSerializer
from br_med.core.utils import get_period_from_request, range_dates


class QuoteListView(generics.ListAPIView):
    serializer_class = QuoteByPeriodSerializer
    period = None

    def get_queryset(self):
        start_at, end_at = get_period_from_request(self.request.query_params)
        self.period = dict(start_at=start_at, end_at=end_at)
        return Quote.objects.filter_by_period(start_at=start_at, end_at=end_at)

    def get_serializer_context(self):
        context = super(QuoteListView, self).get_serializer_context()
        context["period"] = self.period
        return context

    def list(self, request, *args, **kwargs):
        quotes = self.get_queryset()
        context = self.get_serializer_context()
        serializer = self.get_serializer_class()
        serializer = serializer(instance=quotes, many=False, context=context)
        return Response(serializer.data)
