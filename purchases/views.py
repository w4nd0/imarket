from rest_framework import viewsets

from purchases.serializeres import PurchaseSerializer

from .models import Purchase


class PurchaseModelViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
