import graphene
from graphene_django import DjangoObjectType
from users.models import CustomUser


class CustomUserType(DjangoObjectType):
    class Meta:
        model = CustomUser
        fields = "__all__"


class Query(graphene.ObjectType):
    all_users = graphene.List(CustomUserType)

    def resolve_all_users(root, info):
        # We can easily optimize query count in the resolve method
        return CustomUser.objects.all()


