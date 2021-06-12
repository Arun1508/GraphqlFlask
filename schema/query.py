import graphene
from graphene import relay
from flask_graphql_auth import query_jwt_required

from models.genres import Genres as GenresModel
from models.books import Books as BooksModel
from sql_types.books import Books
from auth_mutation import ProtectedUnion, MessageField


class Query(graphene.ObjectType):
    node = relay.Node.Field()

    books_by_name = graphene.List(Books, name=graphene.String())
    books_by_genre = graphene.List(Books, name=graphene.String())
    all_books = graphene.List(Books)
    protected = graphene.Field(type=ProtectedUnion, token=graphene.String())

    @staticmethod
    def resolve_all_books(parent, info, **args):
        books = Books.get_query(info)
        return books.all()

    @staticmethod
    def resolve_books_by_name(parent, info, **args):
        q = args.get('name')
        print(type(q))
        # print("reading Books")
        books_query = Books.get_query(info)
        # books = books_query.filter(BooksModel.name.contains(q)).all()
        books = books_query.filter(BooksModel.name.contains(q)).all()
        print(books)
        return books
        # return dbook

    @staticmethod
    def resolve_books_by_genre(self, info, **args):
        q = args.get("name")
        print(f"in resolver genre {q}")
        books_query = Books.get_query(info)
        print(f'genre {books_query}')
        return books_query.join(GenresModel).filter(GenresModel.name == q).all()

    @query_jwt_required
    def resolve_protected(self, info):
        return MessageField(message="Hello World!")
