# Описание модели авторов

from sqlalchemy import Column, Integer, String, DateTime

from config.config_bd import Base


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    date_of_birth = Column(DateTime)
