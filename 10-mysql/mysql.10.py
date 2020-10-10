import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", passwd="goodtime", database="shopper")
cursor = db.cursor()


sql = "SELECT * FROM customers LIMIT 2 OFFSET 2"

cursor.execute(sql)
results = cursor.fetchall()

for row in results:
  print(row)


