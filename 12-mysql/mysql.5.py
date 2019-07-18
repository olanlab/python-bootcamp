import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", passwd="goodtime", database="shopper")
cursor = db.cursor()

sql = "SELECT * FROM customers WHERE age = %s"
values = (34, )

cursor.execute(sql, values)
results = cursor.fetchall()

for row in results:
  print(row)
