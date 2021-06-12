import graphene

from database.db_session import db_session


from models.books import Books as BooksModel
from sql_types.books import Books, CreateBookInput
from utils.input_to_dictionary import input_to_dictionary




class CreateBook(graphene.Mutation):
    book = graphene.Field(lambda: Books)
    ok = graphene.Boolean()

    class Arguments:
        input = CreateBookInput(required=True)

    @staticmethod
    def mutate(self, info, input):
        data = input_to_dictionary(input)
        book = BooksModel(**data)
        db_session.add(book)
        db_session.commit()
        ok = True
        return CreateBook(book=book, ok=ok)


class Mutation(graphene.ObjectType):
    createBook = CreateBook.Field()
