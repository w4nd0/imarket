from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from utils.permissions import IsOwnerOrSuperUser, IsSuperUser

from carts.serializeres import CartSerializer

from .models import Cart


class CartListViewSet(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSuperUser]


class CartDetailViewSet(generics.RetrieveAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrSuperUser]
