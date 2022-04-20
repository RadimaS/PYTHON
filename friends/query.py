import graphene
from graphene_django import DjangoObjectType
from friends.models import Friend


class FriendType(DjangoObjectType):
    class Meta:
        model = Friend
        fields = "__all__"


class Query(graphene.ObjectType):
    all_friends = graphene.List(FriendType)

    def resolve_all_friends(root, info):
        return Friend.objects.all()


