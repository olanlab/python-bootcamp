import sqlite3

conn = sqlite3.connect('shopper.db')

conn.execute('''CREATE TABLE product (
    id INTEGER PRIMARY KEY,
    product_name TEXT,
    unit_price FLOAT
)''')

conn.commit()
conn.close()