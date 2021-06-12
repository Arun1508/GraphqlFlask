from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from models.genres import Genres as GenresModel


class Genres(SQLAlchemyObjectType):
    class Meta:
        model = GenresModel
        interfaces = (relay.Node,)