from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb://localhost:27017"


def get_mongo_database():
    return MongoClient(uri, server_api=ServerApi('1'))["dataset"]
