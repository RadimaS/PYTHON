from models import Profile, Contacts
from rest_framework import serializers
from follows.models import Follow


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='first_name')
    contacts = ContactsSerializer()

    followed = serializers.SerializerMethodField()

    def get_followed(self, user):
        me = self.context['request'].user
        if me.is_anonymous:
            return False

        return Follow.objects.filter(follower=me, followed=user).exists()

    class Meta:
        model = Profile
        fields = ['id', 'name', 'email', 'status', 'photos', 'followed']
