import json
from dotenv import load_dotenv
from scraping import find_all_data_from_pages
from models import NewPost, Post
from fastapi import FastAPI
import os
import sys

from mongoengine import connect
sys.setrecursionlimit(3000)


load_dotenv()

app = FastAPI()

connect('dark_web',
        host=os.getenv('MONGO_URI'))


def save_posts():
    data = find_all_data_from_pages()
    for post in data:
        Post(**post).save()
    print("haha")
    return "Data inserted"


@app.get("/data")
def get_all_data():
    save_posts()
    data = json.loads(Post.objects.order_by(
        '-Date').to_json())  # order by date
    return data


@app.post("/add_post")
def create_data(data: NewPost):
    post = Post(Title=data.Title, Content=data.Content,
                Author=data.Author, Date=data.Date)
    post.save()
    return post
