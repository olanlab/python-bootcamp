import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", passwd="goodtime", database="shopper")
cursor = db.cursor()

sql = "DELETE FROM customers WHERE age = 34"
cursor.execute(sql)
db.commit()
print(cursor.rowcount, "record(s) deleted")
