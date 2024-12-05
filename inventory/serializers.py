from rest_framework import serializers
from .models import Product, Category
from rest_framework.exceptions import ValidationError

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate_quantity(self, value):
        if value < 0:
            raise ValidationError("Quantity cannot be negative.")
        return value

    def validate_price(self, value):
        if value < 0:
            raise ValidationError("Price cannot be negative.")
        return value
