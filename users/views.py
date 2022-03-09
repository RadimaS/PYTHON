from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import CustomUser
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        users = CustomUser.objects.all()

        serializer = UserSerializer(users, many=True, context={'request': request})
        return Response(data=serializer.data)
