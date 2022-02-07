import os
from mongoengine import connect
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

from models import Post
from scraping import find_all_data_from_pages

from dotenv import load_dotenv
load_dotenv()

app = FastAPI()


connect('dark_web',
        host=os.getenv('MONGO_URI'))


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/data")
def get_all_data():
    data = Post.objects.all()
    return data


class NewPost(BaseModel):
    Title: str
    Content: str
    Author: str
    Date: str


@app.post("/add_post")
def create_data(data: NewPost):
    post = Post(Title=data.Title, Content=data.Content,
                Author=data.Author, Date=data.Date)
    post.save()
    return post


@app.get("/insert_data")
def insert_data():
    data = find_all_data_from_pages()
    for post in data:
        try:
            Post.objects.insert(Title=post['Title'], Content=post['Content'],
                                Author=post['Author'], Date=post['Date']).save()
        except:
            "Error: Cannot insert data"
    return "Data inserted"
