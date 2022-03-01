from rest_framework import serializers

from accounts.models import User
from carts.models import Cart


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "password",
            "email",
            "username",
            "is_superuser",
        ]

        extra_kwargs = {
            "id": {"read_only": True},
            "password": {"write_only": True},
            "email": {"required": False},
            "is_superuser": {"required": False},
        }

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        Cart.objects.create(user=instance)
        return instance


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()
