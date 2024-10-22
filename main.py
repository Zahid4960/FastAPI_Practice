from fastapi import FastAPI

app = FastAPI()

@app.get('/books')
async def read_root():
    return {'message:' 'Hello world'}

@app.get('/my-fav-book-list')
async def fav_book_lists():
    fav_list = ['1. Deyal', '2. Atomic habits']
    return fav_list
