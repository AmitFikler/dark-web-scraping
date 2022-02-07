from mongoengine import Document, StringField
from pydantic import BaseModel


class Post(Document):
    Title = StringField(max_length=120, required=True)
    Content = StringField(required=True)
    Author = StringField(max_length=120, required=True)
    Date = StringField(max_length=120, required=True)


class NewPost(BaseModel):
    Title: str
    Content: str
    Author: str
    Date: str
