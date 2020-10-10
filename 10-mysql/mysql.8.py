import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", passwd="goodtime", database="shopper")
cursor = db.cursor()

sql = "update customers set age = 18 where age = 25"

cursor.execute(sql)
db.commit()

print(cursor.rowcount, " record(s) affected")