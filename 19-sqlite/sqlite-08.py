import sqlite3

conn = sqlite3.connect('shopper.db')

# conn.execute('''ALTER TABLE product
#     ADD COLUMN product_category_id INTEGER
# ''')
             
# conn.execute('''CREATE TABLE product_category (
#     id INTEGER PRIMARY KEY,
#     product_category_name TEXT
# )''')

cursor = conn.cursor()
# cursor.execute("INSERT INTO product_category (product_category_name) VALUES ('Electronics')")
# cursor.execute("INSERT INTO product_category (product_category_name) VALUES ('Furnitures')")
# cursor.execute("INSERT INTO product_category (product_category_name) VALUES ('Stationery')")
# cursor.execute("INSERT INTO product_category (product_category_name) VALUES ('Clothes')")


# cursor.execute("SELECT * from product_category")
# result = cursor.fetchall()
# for row in result:
#     print(row)

# cursor.execute("UPDATE product SET product_category_id = 3 WHERE id = 1")
# cursor.execute("UPDATE product SET product_category_id = 4 WHERE id = 2")
# cursor.execute("UPDATE product SET product_category_id = 2 WHERE id = 3")
# cursor.execute("INSERT INTO product (product_name, product_category_id, unit_price) VALUES ('Laptop', 1, 20000)")
# cursor.execute("INSERT INTO product (product_name, product_category_id, unit_price) VALUES ('TV', 1, 18000)")
cursor.execute("INSERT INTO product (product_name, product_category_id, unit_price) VALUES ('PS', 1, 20980)")

conn.commit()
conn.close()