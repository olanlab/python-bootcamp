import sqlite3

# Connection
conn = sqlite3.connect('shopper.db')

# Cursor
cursor = conn.cursor()
cursor.execute("UPDATE product SET unit_price = unit_price * 1.1 WHERE id = 1")

conn.commit()
conn.close()