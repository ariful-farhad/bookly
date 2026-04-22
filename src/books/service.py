from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from src.books.models import Book, desc
from src.books.schemas import BookCreateModel, BookUpdateModel


class BookService:
    async def get_all_books(self, session: AsyncSession):
        statement = select(Book).order_by(desc(Book.created_at))
        result = await session.exec(statement)
        return result.all()

    async def get_book(self, book_uid: str, session: AsyncSession):
        pass

    async def create_book(self, book_data: BookCreateModel, session: AsyncSession):
        pass

    async def update_book(
        self, book_uid: str, update_data: BookUpdateModel, session: AsyncSession
    ):
        pass

    async def delete_book(self, book_uid: str, session: AsyncSession):
        pass
