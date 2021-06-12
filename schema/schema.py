import graphene
from flask_graphql_auth import AuthInfoField
from schema.query import Query
from schema.mutation import Mutation

from sql_types.genre import Genres
from sql_types.books import Books
from sql_types.characters import Characters


class MessageField(graphene.ObjectType):
    message = graphene.String()


class ProtectedUnion(graphene.Union):
    class Meta:
        types = (MessageField, AuthInfoField)

    @classmethod
    def resolve_type(cls, instance, info):
        return type(instance)


schema = graphene.Schema(query=Query, mutation=Mutation, types=[Genres, Books, Characters])
