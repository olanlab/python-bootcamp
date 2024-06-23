import sqlite3

# Connection
conn = sqlite3.connect("shopper.db")

# Cursor
cursor = conn.cursor()
cursor.execute(
    """SELECT COUNT(1), AVG(unit_price), MAX(unit_price), MIN(unit_price) 
        from product"""
)

result = cursor.fetchone()
print(result)

conn.commit()
conn.close()
