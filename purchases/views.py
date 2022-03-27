from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView
from carts.models import Cart

from purchases.serializeres import PurchaseSerializer
from utils.mixins import UpdateRetrieveViewSet

from .models import Purchase

class CreatePurchaseView(CreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self,request):
        purchase = Purchase.objects.create(user_id=request.user.pk)

        cart = get_object_or_404(Cart, user_id=request.user.pk)

        items = cart.items.all()

        for item in items:
            item.purchase_id = purchase.id
            item.save()
        
        return Response({'msg':'ok'}, status=status.HTTP_201_CREATED)


class PurchaseListCreateView(UpdateRetrieveViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def filter_queryset(self, queryset):
        user = self.request.user

        if not user.is_superuser:
            queryset = queryset.filter(user=self.request.user)

        return super().filter_queryset(queryset)

    def get_object(self):
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}

        object = get_object_or_404(Purchase, **filter_kwargs)

        if object.user.id != self.request.user.id and not self.request.user.is_superuser:
            raise PermissionDenied("You don't have permission to access this purchase")

        return object

