import mysql.connector

connection = mysql.connector.connect(user='root', host='localhost', charset="utf8mb4",  database="shopper" )

cursor = connection.cursor()
 
# INSERT 
sql = "INSERT INTO product (product_name, sku, quantity, unit_price) VALUES ( %s, %s, %s, %s)"
val = ("เก้าอี้นวดไฟฟ้า 2", "OL-0005", 12, 500.00)
cursor.execute(sql, val)

connection.commit()

print(cursor.rowcount, "record(s) affected")

cursor.close()
connection.close()

