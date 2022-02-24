from rest_framework import viewsets

from products.serializeres import ProductSerializer

from .models import Product


class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
