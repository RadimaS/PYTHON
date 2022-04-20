from graphene import ObjectType, String, Schema
from users.query import Query as UsersQuery


class Query(UsersQuery, ObjectType):
    hello = String(name=String(default_value="stranger"))
    goodbye = String()


schema = Schema(query=Query)