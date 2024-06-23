import sqlite3

# Connection
conn = sqlite3.connect('shopper.db')

# Cursor
cursor = conn.cursor()
cursor.execute("INSERT INTO product (id, product_name, unit_price) VALUES (?, ?, ?)", (1, 'Pencil', 20))

data = [
    (2, 'Shirt', 300),
    (3, 'Chair', 350),
    (4, 'TV', 12800)
]

cursor.executemany("INSERT INTO product (id, product_name, unit_price) VALUES (?, ?, ?)", data)

conn.commit()
conn.close()