from rest_framework import viewsets

from carts.serializeres import CartSerializer

from .models import Carts


class CartModelViewSet(viewsets.ModelViewSet):
    queryset = Carts.objects.all()
    serializer_class = CartSerializer
