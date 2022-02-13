from database import database
from scraping import find_all_data_from_pages
from fastapi import FastAPI

############## SERVER ################
app = FastAPI()


############## INITIALIZE DB ################
database.Database.initialize()


def save_posts():
    data = find_all_data_from_pages()
    for post in data:
        database.Database.insert("post", post)
    return "Data inserted"

############## GET ALL PASTE /data ################


@app.get("/data")
def get_all_data():
    save_posts()
    data = database.Database.find("post", {})
    return data


# Analytics
# common words
@app.get("/analysis/common_Words_content")
def get_dark_common_words_content():
    return database.Database.common_word_content("post")


@app.get("/analysis/common_Words_title")
def get_dark_common_words_title():
    return database.Database.common_word_title("post")
# Total pastes


@app.get("/analysis/total_amount")
def get_total_pastes_amount():
    return database.Database.count("post")

# Pastes per author


@app.get("/analysis/per_author")
def get_authors_analysis():
    return database.Database.get_authors_analysis("post")
