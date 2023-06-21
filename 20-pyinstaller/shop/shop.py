import sqlite3
import os
import sys

if getattr(sys, 'frozen', False):
     extDataDir = sys._MEIPASS
     extDataDir  = os.path.join(extDataDir, 'shopper.db')      
else:
     extDataDir = os.getcwd()
     extDataDir = os.path.join(extDataDir, 'shopper.db') 
print(f"path of extDataDir is {extDataDir}")

# Connection
conn = sqlite3.connect(extDataDir)

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