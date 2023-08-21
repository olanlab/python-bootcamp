import sqlite3

# Connection
conn = sqlite3.connect('shopper.db')

# Cursor
cursor = conn.cursor()
cursor.execute("SELECT * from product, product_category WHERE product.product_category_id = product_category.id ORDER BY product.id DESC LIMIT 3")
result = cursor.fetchall()

for row in result:
    print(row)

conn.close()