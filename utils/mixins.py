from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class RetrieveUpdateDestroyViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    pass
