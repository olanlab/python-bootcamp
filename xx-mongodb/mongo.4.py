import pymongo

mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")

db = mongoClient["shopper"]
collection = db["customers"]

result = collection.find_one()
print(result)

docs = collection.find({})
for doc in docs:
  print(doc)
