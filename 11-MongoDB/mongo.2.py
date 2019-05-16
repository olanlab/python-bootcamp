import pymongo

mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")

db = mongoClient["shopper"]
collection = db["customers"]