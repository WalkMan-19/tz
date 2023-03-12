from rest_framework import generics

from core.models import User
from core.serializers import CreateUserSerializer


class CreateUserView(generics.CreateAPIView):
    model = User
    serializer_class = CreateUserSerializer
