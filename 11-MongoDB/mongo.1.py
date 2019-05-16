import pymongo

mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
dbs = mongoClient.list_database_names()

print(dbs)
if "shopper" in dbs:
  print("The database exists.")

