from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get('/books')
async def read_root():
    return {'message:' 'Hello world'}

class BookCreateModel(BaseModel):
    title: str
    author: str

@app.post('/book-create')
async def book_create(book_data: BookCreateModel):
    return {
        'title': book_data.title,
        'author': book_data.author
    }
