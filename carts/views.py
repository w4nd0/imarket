from rest_framework import viewsets

from carts.serializeres import CartSerializer

from .models import Cart


class CartModelViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
