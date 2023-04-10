import mysql.connector

connection = mysql.connector.connect(user='root', host='localhost', charset="utf8mb4",  database="shopper" )

cursor = connection.cursor()

# UPDATE
sql = "UPDATE product SET product_name = %s, sku = %s , quantity = %s, unit_price = %s WHERE id = %s"
val = ("เก้าอี้นวดไฟฟ้า XXX", "OL-0004", 1, 1500.00, 8)
cursor.execute(sql, val)
connection.commit()

print(cursor.rowcount, "record(s) affected")

connection.close()

