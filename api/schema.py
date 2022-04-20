from graphene import ObjectType, String, Schema
from users.query import Query as UsersQuery
from profiles.mutations import ProfileMutation


class Query(UsersQuery, ObjectType):
    hello = String(name=String(default_value="stranger"))
    goodbye = String()


class Mutation(ProfileMutation):
    pass


schema = Schema(query=Query, mutation=Mutation)
