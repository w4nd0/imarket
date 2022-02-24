from rest_framework import serializers
from carts.models import Carts


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carts
        fields = "__all__"
