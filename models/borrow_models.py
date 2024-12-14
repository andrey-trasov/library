# Описание модели выдача

from sqlalchemy import Column, Integer, String, Text, ForeignKey, Date
from sqlalchemy.orm import relationship

from config.config_bd import Base


class Borrow(Base):
    __tablename__ = 'borrows'
    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    readers_name = Column(String)
    issue_date = Column(Date)
    return_date = Column(Date)

    book = relationship("Book")
