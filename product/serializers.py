from rest_framework import serializers
from .models import Product, EnterProduct, ExpenseProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class EnterProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnterProduct
        fields = "__all__"


class ExpenseProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseProduct
        fields = "__all__"
