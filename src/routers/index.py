from src.routers.books import book_router
from fastapi import APIRouter

baseRouter = APIRouter(
    prefix="/api",
)

baseRouter.include_router(book_router.router)
