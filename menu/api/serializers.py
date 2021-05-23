from rest_framework import serializers
from menu.models import Dish, Order, Table


class DishSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dish
        exclude = ('id',)

    def validate_price(self, price: float) -> float:
        if price <= 0:
            raise serializers.ValidationError(
                "Price should be higher than 0."
            )
        return price

    def validate_weight(self, weight: float) -> float:
        if weight <= 0:
            raise serializers.ValidationError(
                "Weight should be higher than 0."
            )
        return weight


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'

    def validate_diners(self, diners: int) -> int:
        if diners <= 0:
            raise serializers.ValidationError(
                "Number of diners has to be 1 or greater."
            )
        return diners


class TableSerializer(serializers.ModelSerializer):

    class Meta:
        model = Table
        fields = '__all__'
