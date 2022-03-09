from datetime import datetime

from django.db.models import Q
from rest_framework import viewsets
from rest_framework.exceptions import APIException

from api.serializers import DualSerializerViewSet
from follows.models import Follow

from follows.serializers import FollowSerializer


class FollowViewSet(DualSerializerViewSet):
    queryset = Follow.objects.all()

    serializer_classes = {
        'create': FollowSerializer,
        'update': FollowSerializer
    }

    default_serializer_class = FollowSerializer
