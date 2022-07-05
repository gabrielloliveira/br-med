from rest_framework import serializers

from br_med.core.enums import CurrencyEnum
from br_med.core.models import Quote


class CurrencySerializer(serializers.Serializer):
    currency = serializers.CharField()
    value = serializers.DecimalField(max_digits=100, decimal_places=20)

    def create(self, validated_data):
        raise NotImplementedError

    def update(self, instance, validated_data):
        raise NotImplementedError


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ["date", "value"]


class QuoteByPeriodSerializer(serializers.Serializer):
    period = serializers.SerializerMethodField()
    results = serializers.SerializerMethodField()

    def create(self, validated_data):
        raise NotImplementedError

    def update(self, instance, validated_data):
        raise NotImplementedError

    def get_period(self, obj):
        return self.context.get("period")

    def get_results(self, obj):
        period = self.context.get("period")
        range_period = [period["start_at"], period["end_at"]]
        results = []
        for currency in CurrencyEnum.choices:
            data = dict()
            key = currency[0]

            quotes = Quote.objects.filter(currency=key, date__range=range_period).order_by("-date")
            quotes_serializer = QuoteSerializer(quotes, many=True).data

            data[key] = quotes_serializer
            results.append(data)
        return results
