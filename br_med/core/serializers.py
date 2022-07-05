from rest_framework import serializers

from br_med.core.models import Quote


class CurrencySerializer(serializers.Serializer):
    currency = serializers.CharField()
    value = serializers.DecimalField(max_digits=100, decimal_places=20)

    def create(self, validated_data):
        raise NotImplementedError

    def update(self, instance, validated_data):
        raise NotImplementedError


class QuoteSerializer(serializers.Serializer):
    date = serializers.CharField()
    currencies = CurrencySerializer(many=True)


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
        results = []
        range_dates = self.context.get("range_dates")
        for date in range_dates:
            data = dict(date=date, currencies=self.context["queryset"].filter(date=date))
            nested = QuoteSerializer(data, many=False)
            results.append(nested.data)
        return results
