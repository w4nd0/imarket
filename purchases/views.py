from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated

from purchases.serializeres import PurchaseSerializer
from utils.mixins import UpdateRetrieveViewSet

from .models import Purchase


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

