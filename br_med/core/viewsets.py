from rest_framework import generics

from br_med.core.models import Quote
from br_med.core.serializers import QuoteSerializer
from br_med.core.utils import get_period_from_request


class QuoteListView(generics.ListAPIView):
    serializer_class = QuoteSerializer

    def get_queryset(self):
        start_at, end_at = get_period_from_request(self.request.query_params)
        return Quote.objects.filter_by_period(start_at=start_at, end_at=end_at)
