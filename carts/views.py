from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.exceptions import PermissionDenied
from rest_framework import viewsets
from carts.serializeres import CartSerializer
from utils.mixins import UpdateRetrieveViewSet

from .models import Cart
from rest_framework.response import Response
from rest_framework import status


class CartUpdateRetrieveView(UpdateRetrieveViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # def update(self, instance, validated_data):
    #     print(validated_data)

    #     return Response(
    #         {"msg": "ok"}, status=status.HTTP_200_OK
    #     )

    def filter_queryset(self, queryset):
        user = self.request.user

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


# class StudentViewSet(viewsets.ViewSet):

#     def create(self, request):
#         print(request)
#         return Response(
#             {"msg": "ok"}, status=status.HTTP_200_OK
#         )

#     def list(self, request):
#         print(request)
#         return Response(
#             {"msg": "ok"}, status=status.HTTP_200_OK
#         )

#     def retrieve(self, request, pk=''):
#         print(request)
#         return Response(
#             {"msg": "ok"}, status=status.HTTP_200_OK
#         )

#     def update(self, request, pk=''):
#         print(request)
#         return Response(
#             {"msg": "ok"}, status=status.HTTP_200_OK
#         )
