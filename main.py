from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/books')
async def read_root():
    return {'message:' 'Hello world'}

@app.get('/greet')
async def greet(name: Optional[str] = 'User', age: int = 0) -> object:
    return {'message:' f'hello {name} your age is: {age}'}

@app.get('/my-fav-book-list')
async def fav_book_lists():
    fav_list = ['1. Deyal', '2. Atomic habits']
    return fav_list

class BookCreateModel(BaseModel):
    title: str
    author: str

@app.post('/book-create')
async def book_create(book_data: BookCreateModel):
    return {
        'title': book_data.title,
        'author': book_data.author
    }
