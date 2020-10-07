from rest_framework import viewsets
from .serializers import ProductSerializer
from .models import Product
from rest_framework.permissions import IsAuthenticated


class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

