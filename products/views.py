from rest_framework import viewsets

from products.serializeres import ProductSerializer

from .models import Products


class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
