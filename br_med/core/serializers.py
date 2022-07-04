from rest_framework import serializers


class CurrencySerializer(serializers.Serializer):
    currency = serializers.CharField()
    value = serializers.DecimalField(max_digits=100, decimal_places=20)

    def create(self, validated_data):
        raise NotImplementedError

    def update(self, instance, validated_data):
        raise NotImplementedError


class QuoteSerializer(serializers.Serializer):
    period = serializers.SerializerMethodField()
    results = serializers.SerializerMethodField()

    def create(self, validated_data):
        raise NotImplementedError

    def update(self, instance, validated_data):
        raise NotImplementedError

    @staticmethod
    def get_results(obj):
        currencies = obj.values("currency", "value")
        return CurrencySerializer(currencies, many=True).data

    def get_period(self, obj):
        return self.context.get("period")
