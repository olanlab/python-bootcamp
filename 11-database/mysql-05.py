import mysql.connector

connection = mysql.connector.connect(user='root', host='localhost', charset="utf8mb4",  database="shopper" )

cursor = connection.cursor()

# DELETE
sql = "DELETE FROM product WHERE sku=%s"
val = ("OL-0005", )
cursor.execute(sql, val)
connection.commit()

print(cursor.rowcount, "record(s) affected")

connection.close()

