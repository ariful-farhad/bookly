from fastapi import FastAPI, Header
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
async def asdf():
    print("hello world")
    return {"hello": "world"}

# @app.get('/greet')
# async def greetme():
#     return {"message": "hi there"}

# @app.get('/greet')
# async def greeta(name:str) -> dict:
#     return {"message": f"hello {name }"}


@app.get('/greet')
async def greetQuery(name: Optional[str] = None, age: Optional[str] = None):
    if name and age:
        return {"message": f"hello {name}", "age": age}
    if age and not name:
        return {"message": f"your age is {age}"}
    return {"Message": "hello there"}

# @app.get('/greet/{name}')
# async def greet(name:str) -> dict:
#     return {"message": f"hello {name }"}

# @app.get('/greet/{name}')
# async def greetvarparam(name: str, age: int):
#     return {"name": name, "age": age}

@app.get('/greet/{name}')
async def greetvarparam(name: str, age: Optional[int] = None) -> dict:
    if age:
        return {"name": name, "age": age}
    return {"name": name}

class BookCreateModel(BaseModel):
    title: str
    author: str

@app.post('/create_book')
async def create_book(book_data: BookCreateModel):
    return {
        "title": book_data.title,
        "author": book_data.author
    }

@app.get('/get_headers', status_code=500)
async def get_headers(
    accept:str = Header(None),
    content_type: str = Header(None),
    user_agent: str = Header(None),
    host: str = Header(None)
):
    request_headers = {}
    request_headers["Accept"] = accept
    request_headers["Content_type"] = content_type
    request_headers["User_agent"] = user_agent
    request_headers["Host"] = host
    return request_headers