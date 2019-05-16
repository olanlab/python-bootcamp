import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", passwd="goodtime", database="shopper")
cursor = db.cursor()

sql = "SELECT * FROM customers"

cursor.execute(sql)
# results = cursor.fetchall()
results = cursor.fetchone()

for row in results:
  print(row)
