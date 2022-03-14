from rest_framework import serializers
from carts.models import Cart
from products.serializeres import ProductSerializer


class NewProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    quantity = serializers.IntegerField()


class CartSerializer(serializers.ModelSerializer):
    products = NewProductSerializer(many=True)

    class Meta:
        model = Cart
        fields = ['products']

class ViewCartSerializer(serializers.Serializer):
    products = ProductSerializer(many=True)
    total = serializers.IntegerField()


    