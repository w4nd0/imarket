from rest_framework import serializers
# from carts.models import Cart
from rest_framework.response import Response
from rest_framework import status


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    quantity = serializers.IntegerField()


class CartSerializer(serializers.Serializer):
    products = ProductSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        print(validated_data)

        return Response(
            {"msg": "ok"}, status=status.HTTP_200_OK
        )
# class CartSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Cart
#         fields = ["id", "total", "user"]
