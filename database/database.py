from pymongo import MongoClient
from bson import json_util
import json

import os
import dotenv


dotenv.load_dotenv()


class Database(object):
    URI = os.getenv('MONGO_URI')
    DATABASE = None

    @staticmethod
    def initialize():
        client = MongoClient(host=Database.URI)
        Database.DATABASE = client.dark_web

    @staticmethod
    def insert(collection, data):
        return Database.DATABASE[collection].update_one({**data}, {"$set": {**data}}, upsert=True)

    @ staticmethod
    def find(collection, query):
        return parse_json(Database.DATABASE[collection].find(query).sort("Date", -1))

    @ staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

    @ staticmethod
    def count(collection):
        return Database.DATABASE[collection].count_documents({})

    @ staticmethod
    def common_word_title(collection):
        analytics_obj = {
            "total_pastes_bitcoin": Database.DATABASE[collection].count_documents({"Title": {'$regex': "bitcoin", '$options': 'i'}}),
            "total_pastes_porn": Database.DATABASE[collection].count_documents({"Title": {'$regex': "porn", '$options': 'i'}}),
            "total_pastes_gun": Database.DATABASE[collection].count_documents({"Title": {'$regex': "gun", '$options': 'i'}}),
            "total_pastes_creditcard": Database.DATABASE[collection].count_documents({"Title": {'$regex': "creditcard", '$options': 'i'}}),
            "total_pastes_onion": Database.DATABASE[collection].count_documents({"Title": {'$regex': "onion", '$options': 'i'}}),
            "total_pastes_drug": Database.DATABASE[collection].count_documents({"Title": {'$regex': "drug", '$options': 'i'}}),
            "total_pastes_hack": Database.DATABASE[collection].count_documents({"Title": {'$regex': "hack", '$options': 'i'}}),
            "total_pastes_leak": Database.DATABASE[collection].count_documents({"Title": {'$regex': "leak", '$options': 'i'}}),
            "total_pastes_child":  Database.DATABASE[collection].count_documents({"Title": {'$regex': "child", '$options': 'i'}}),
            "total_pastes_dark": Database.DATABASE[collection].count_documents({"Title": {'$regex': "dark", '$options': 'i'}}),
        }
        return analytics_obj

    @ staticmethod
    def get_authors_analysis(collection):
        return list(Database.DATABASE[collection].aggregate([
            {"$group": {"_id": "$Author",
                        "Total": {"$sum": 1}}}
        ]))

    @ staticmethod
    def common_word_content(collection):
        analytics_obj = {
            "total_pastes_bitcoin": Database.DATABASE[collection].count_documents({"Content": {'$regex': "bitcoin", '$options': 'i'}}),
            "total_pastes_porn": Database.DATABASE[collection].count_documents({"Content": {'$regex': "porn", '$options': 'i'}}),
            "total_pastes_gun": Database.DATABASE[collection].count_documents({"Content": {'$regex': "gun", '$options': 'i'}}),
            "total_pastes_creditcard": Database.DATABASE[collection].count_documents({"Content": {'$regex': "creditcard", '$options': 'i'}}),
            "total_pastes_onion": Database.DATABASE[collection].count_documents({"Content": {'$regex': "onion", '$options': 'i'}}),
            "total_pastes_drug": Database.DATABASE[collection].count_documents({"Content": {'$regex': "drug", '$options': 'i'}}),
            "total_pastes_hack": Database.DATABASE[collection].count_documents({"Content": {'$regex': "hack", '$options': 'i'}}),
            "total_pastes_leak": Database.DATABASE[collection].count_documents({"Content": {'$regex': "leak", '$options': 'i'}}),
            "total_pastes_child":  Database.DATABASE[collection].count_documents({"Content": {'$regex': "child", '$options': 'i'}}),
            "total_pastes_dark": Database.DATABASE[collection].count_documents({"Content": {'$regex': "dark", '$options': 'i'}}),
        }
        return analytics_obj


##### HELPER #####


def parse_json(data):
    return json.loads(json_util.dumps(data))
