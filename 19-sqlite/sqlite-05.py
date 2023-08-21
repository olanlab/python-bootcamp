import sqlite3

# Connection
conn = sqlite3.connect('shopper.db')

# Cursor
cursor = conn.cursor()
cursor.execute("DELETE from product WHERE id > ?", (3,))

conn.commit()
conn.close()