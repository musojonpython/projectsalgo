from rest_framework import viewsets
from .serializers import ProductSerializer, EnterProductSerializer, ExpenseProductSerializer
from .models import Product, EnterProduct, ExpenseProduct
from rest_framework.permissions import IsAuthenticated


class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class EnterProductModelViewSet(viewsets.ModelViewSet):
    queryset = EnterProduct.objects.all()
    serializer_class = EnterProductSerializer


class ExpenseProductModelViewSet(viewsets.ModelViewSet):
    queryset = ExpenseProduct.objects.all()
    serializer_class = ExpenseProductSerializer
