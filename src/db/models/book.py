from sqlalchemy import Column, Integer, String

from src.db.config import Base


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    author = Column(String(100), nullable=False)
    release_year = Column(Integer, nullable=False)
