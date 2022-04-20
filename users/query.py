import graphene
from graphene_django import DjangoObjectType
from users.models import CustomUser


class CustomUserType(DjangoObjectType):
    class Meta:
        model = CustomUser
        fields = "__all__"


def Q():
    pass


class Query(graphene.ObjectType):
    all_users = graphene.List(CustomUserType)
    search_by_value = graphene.List(CustomUserType, value=graphene.String(required=True))

    def resolve_all_users(root, info):
        # We can easily optimize query count in the resolve method
        return CustomUser.objects.all()

    def resolve_search_by_value(root, info, value):
        users = CustomUser.objects.filter(Q(first_name__startswith=value)| Q(last_name__startswith=value)|Q(email__startswith=value)|Q(username__startswith=value))
        return users