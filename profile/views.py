from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.models import CustomUser
from users.serializers import StatusSerializer
from .models import Profile
from .serializers import ProfileSerializer


class ProfilesViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileStatusViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = StatusSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request.user.status = serializer.data['status']
        request.user.save()

        return Response(status=status.HTTP_200_OK)

