from rest_framework import viewsets

from purchases.serializeres import PurchaseSerializer

from .models import Purchases


class PurchaseModelViewSet(viewsets.ModelViewSet):
    queryset = Purchases.objects.all()
    serializer_class = PurchaseSerializer
