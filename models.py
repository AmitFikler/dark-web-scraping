from mongoengine import Document, StringField


class Post(Document):
    Title = StringField(max_length=120, required=True)
    Content = StringField(required=True)
    Author = StringField(max_length=120, required=True)
    Date = StringField(max_length=120, required=True)
