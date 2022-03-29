from django.shortcuts import get_object_or_404
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from carts.models import Cart
from products.models import Product
from carts.serializeres import CartSerializer, ViewCartSerializer
from rest_framework.response import Response
from rest_framework import status


class UpdateCartView(mixins.UpdateModelMixin, GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user_id=self.request.user.id)
        return obj

    def update(self, request):
        serializer = self.get_serializer(data=request.data)
        
        # TODO Mudar o raise_exceprion
        serializer.is_valid(raise_exception=True)

        cart = self.get_object()
        
        products = request.data['products']

        for product in products:
            p = Product.objects.get(id=product['id'])

            cart.products.add(p, through_defaults={ 'quantity': product['quantity'], 
                                                    'unit_price': p.price})
        
            cart.total = cart.total + product['quantity'] * p.price            
            cart.save()

        return Response(
            {"msg": "ok"}, status=status.HTTP_200_OK
        )


class ReadCartView(viewsets.ReadOnlyModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = ViewCartSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def filter_queryset(self, queryset):
        user = self.request.user
        print('ola')

        if not user.is_superuser:
            queryset = queryset.filter(user=self.request.user)

        return super().filter_queryset(queryset)

    def get_object(self):
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}

        object = get_object_or_404(Cart, **filter_kwargs)

        if object.user.id != self.request.user.id \
           and not self.request.user.is_superuser:
            raise PermissionDenied("You don't have permission \
                                    to access this Cart")

        return object
