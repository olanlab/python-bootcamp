import pymongo

mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")

db = mongoClient["shopper"]
collection = db["customers"]

filter = { "age": 20 }
data = { "$set": { "age": 25 } }

collection.update_one(filter, data)

#print "customers" after the update:
for x in collection.find():
  print(x)
