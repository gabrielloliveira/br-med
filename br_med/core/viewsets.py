import datetime

from rest_framework import generics

from br_med.core.models import Quote
from br_med.core.serializers import QuoteSerializer


class QuoteListView(generics.ListAPIView):
    serializer_class = QuoteSerializer

    def get_query_params_formatted(self) -> tuple:
        today = str(datetime.date.today())
        start_at = self.request.query_params.get("start_at", today)
        end_at = self.request.query_params.get("end_at", today)

        start_at = datetime.datetime.strptime(start_at, "%Y-%m-%d").date()
        end_at = datetime.datetime.strptime(end_at, "%Y-%m-%d").date()

        return start_at, end_at

    def get_queryset(self):
        start_at, end_at = self.get_query_params_formatted()
        return Quote.objects.filter_by_period(start_at=start_at, end_at=end_at)
