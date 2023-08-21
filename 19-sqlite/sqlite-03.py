import sqlite3

# Connection
conn = sqlite3.connect('shopper.db')

# Cursor
cursor = conn.cursor()
cursor.execute("SELECT * from product WHERE id > 0")
result = cursor.fetchall()

for row in result:
    print(row)

conn.close()