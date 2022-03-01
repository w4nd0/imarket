from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED
from rest_framework.views import APIView
from utils.permissions import IsOwnerOrSuperUser, IsSuperUser

from accounts.models import User
from accounts.serializeres import LoginSerializer, UserSerializer


class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSuperUser]


class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrSuperUser | IsSuperUser]


class LoginUserView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

        user = authenticate(**serializer.data)

        if user:
            token = Token.objects.get_or_create(user=user)[0]

            return Response({"token": token.key})

        return Response(
            {"error": "user not found"}, status=HTTP_401_UNAUTHORIZED
        )
