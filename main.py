import os
from mongoengine import connect
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

from models import NewPost, Post
from scraping import find_all_data_from_pages

from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

connect('dark_web',
        host=os.getenv('MONGO_URI'))


def save_all_posts():
    data_length = Post.objects.count()
    data = find_all_data_from_pages()
    if data_length == 0:
        for post in data:
            Post(**post).save()
    else:
        for post in data[data_length + 1:]:
            Post(**post).save()
    return "Data inserted"


save_all_posts()


@app.get("/data")
def get_all_data():
    data = Post.objects.all()
    return data


@app.post("/add_post")
def create_data(data: NewPost):
    post = Post(Title=data.Title, Content=data.Content,
                Author=data.Author, Date=data.Date)
    post.save()
    return post
