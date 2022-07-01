from rest_framework import serializers

from br_med.core.models import Quote


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = [
            "uuid",
            "date",
            "currency",
            "value",
        ]
