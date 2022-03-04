from rest_framework.mixins import (UpdateModelMixin,
                                   RetrieveModelMixin)
from rest_framework.viewsets import GenericViewSet


class UpdateRetrieveViewSet(
      UpdateModelMixin,
      RetrieveModelMixin,
      GenericViewSet
):
    pass
