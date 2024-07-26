# for this we need .env file
import os
import sys

import certifi
import pymongo

from src.constant import *
from src.exception import CustomException

ca = certifi.where()

class MongoDbClient:
    Client = None

    def __init__(self,database_name = MONGO_DATA_BASE_NAME) -> None:
        try:
            if MongoDbClient.Client is None:
                mongo_db_url = os.getenv("MONGODB_URL")
                if mongo_db_url is None:
                    raise Exception("Environment Key : MONGODB_URL is not set.")
                MongoDbClient.Client = pymongo.MongoClient(mongo_db_url,tlsCAFile = ca)
            self.Client = MongoDbClient.Client
            self.database = self.Client[database_name]
            self.database_name = database_name
        except Exception as e:
            raise CustomException(e, sys)

        