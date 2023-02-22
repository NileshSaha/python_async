from fastapi import Depends
from src.db.dals.book_dal import BookDAL
from dependencies import get_book_dal


class BookController:
    def __init__(self):
        pass

    async def create_books(self, request, book_dal: BookDAL = Depends(get_book_dal)):
        return {'hello': request}
