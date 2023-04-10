import mysql.connector

connection = mysql.connector.connect(user='root', host='localhost', charset="utf8mb4",  database="shopper" )

# SELECT
cursor = connection.cursor()
sql = "SELECT * FROM product ORDER BY %s asc LIMIT %s OFFSET %s "
val = ("unit_price", 2,0)

cursor.execute(sql, val)
result = cursor.fetchall()

for x in result:
  print(x)

connection.close()