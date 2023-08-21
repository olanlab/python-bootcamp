import sqlite3

# Connection
conn = sqlite3.connect('shopper.db')

# Cursor
cursor = conn.cursor()
cursor.execute('''SELECT product_category_name, count(1), MIN(unit_price), MAX(unit_price), AVG(unit_price)
from product, product_category 
WHERE product.product_category_id = product_category.id 
GROUP BY product.product_category_id
HAVING count(1) > 0
''')
result = cursor.fetchall()

for row in result:
    print(row)

conn.close()