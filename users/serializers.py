from .models import CustomUser
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    created_at = serializers.CharField(source='date_joined')

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'created_at']

