import pymongo

mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")

db = mongoClient["shopper"]
collection = db["customers"]

filter = { "age": 34 }

# collection.delete_one(filter)
result = collection.delete_many(filter)
print(result.deleted_count, " documents deleted.")
