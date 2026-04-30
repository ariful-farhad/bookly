from fastapi import FastAPI
from src.db.main import init_db
from src.books.routes import book_router
from src.auth.routes import auth_router
from contextlib import asynccontextmanager


@asynccontextmanager
async def life_span(app: FastAPI):
    print("Server is starting .... ")
    await init_db()
    yield
    print("Server is ending .... ")


version = "v1"

app = FastAPI(
    version=version,
    title="Bookly",
    description="A REST API for a book review web service",
    lifespan=life_span,
)
app.include_router(book_router, prefix=f"/api/{version}/books", tags=["bookly"])
app.include_router(auth_router, prefix=f"/api/{version}/auth", tags=["auth"])
