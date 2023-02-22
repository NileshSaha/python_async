from typing import Optional, List

from fastapi import APIRouter, Depends, Response
from pydantic import BaseModel, Field
from src.db.dals.book_dal import BookDAL
from src.db.models.book import Book
from src.requests.books.BookRequest import BookRequest
from src.controllers.api.BookController import BookController
from dependencies import get_book_dal

router = APIRouter(
    prefix='/books',
    tags=['books']
)


class Todo(BaseModel):
    title: str
    description: Optional[str]
    priority: int = Field(gt=0, lt=6, description='Priority must be between 1 to 5')
    complete: bool


@router.post("/", )
# async def create_book(name: str, author: str, release_year: int, book_dal: BookDAL = Depends(get_book_dal)):
#     return await book_dal.create_book(name, author, release_year)
async def create_book(request: BookRequest,
                      book_controller: BookController = Depends(BookController)):
    return await book_controller.create_books(request)
    # return request


@router.put("/{book_id}")
async def update_book(book_id: int,
                      name: Optional[str] = None,
                      author: Optional[str] = None,
                      release_year: Optional[int] = None,
                      book_dal: BookDAL = Depends(get_book_dal)):
    return await book_dal.update_book(book_id, name, author, release_year)


# @router.get("/books")
# async def get_all_books(book_dal: BookDAL = Depends(get_book_dal)) -> List[Book]:
#     return await book_dal.get_all_books()
