# Описание модели книг

from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from config.config_bd import Base


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(Text)
    author_id = Column(Integer, ForeignKey('authors.id'),)
    number_books = Column(Integer)

    author = relationship("Author")
