from pymongo import MongoClient


class Mongo:
    __connection_string = None
    __client = None
    __db = None
    __coll = None

    def __init__(self):
        self.__connection_string = "mongodb+srv://deneme1:x6g41qFZYpoFIGeO@test.phmmdhs.mongodb.net/?retryWrites=true&w=majority"

    def connect_database(self):
        self.__client = MongoClient(self.__connection_string)
        self.__db = self.__client["test"]
        self.__coll = self.__db["test_device"]
        print(
            f"Connected to db {self.__db.name} with collection : {self.__coll.name}")

    def close_connection(self):
        self.__client.close()
        print("db connection closed..")

    def insert_data(self, message):
        print("message insterted : ", message)
        return self.__coll.insert_one(message)

    def update_message(self, imei, message):
        print("Device : ", imei, " Updated message : ", message)
        return self.__coll.update_one({"imei": imei}, {"$set": message})

    def get_any_message(self, params={}):
        return list(self.__coll.find_one(params))

    def get_all_messages(self, params={}):
        return list(self.__coll.find(params))
