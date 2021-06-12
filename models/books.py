from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship

from database.base import Base
from models.genres import Genres


class Books(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    author = Column(String)
    genre_id = Column(Integer, ForeignKey('genres.id'))
    genre = relationship(
        Genres,
        backref=backref('books', uselist=True, cascade='delete,all')
    )
