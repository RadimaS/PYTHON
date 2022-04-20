import graphene
from graphene_django import DjangoObjectType
from contacts.models import Contact


class ContactType(DjangoObjectType):
    class Meta:
        model = Contact
        fields = "__all__"


class Query(graphene.ObjectType):
    all_contacts = graphene.List(ContactType)

    def resolve_all_contacts(root, info):
        return Contact.objects.all()


