from fastapi import FastAPI, Query, status
from fastapi.exceptions import HTTPException
from typing import List

from src.books.schemas import Book, BookUpdateModel
from src.books.book_data import books

app = FastAPI()
