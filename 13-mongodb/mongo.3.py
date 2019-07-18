import pymongo

mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")

db = mongoClient["shopper"]
collection = db["customers"]

customer = { "name": "Olan Samritjiarapon", "age": 34 }
result = collection.insert_one(customer)
print(result.inserted_id)

# customers = [{ "name": "Olan Samritjiarapon", "age": 34 }, { "name": "Jame jojoe", "age": 20 }]
# result = collection.insert_many(customers)
# print(result.inserted_ids)
