from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from utils.permissions import IsSuperUserOrReadOnly

from products.serializeres import ProductSerializer

from .models import Product


class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSuperUserOrReadOnly]
