from pymongo import MongoClient

db = object()


class DataBaseManager(object):

    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.client = None


    def connect(self):
        global db
        try:
            self.client = MongoClient(self.connection_string)
        except:
            print("Failed to connect to the database")

        db = self.client["models"]

        return db
