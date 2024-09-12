import sqlite3

# Connection
conn = sqlite3.connect('shopper.db')
try:
    # Begin the transaction
    conn.execute("BEGIN")
    cursor = conn.cursor()

    # Perform multiple database operations
    cursor.execute("INSERT INTO product (product_name, unit_price) VALUES (?, ?)", ("Sony Playstation 5", 15000.00))
    cursor.execute("INSERT INTO product (product_name, unit_price) VALUES (?, ?)", ("Sony Playstation 4", 8000.00))
    # cursor.execute("INSERT INTO product (product_name, unit_price) VALUES (?, ?)", ("Sony Playstation 4", "Game Controller", 8000.00))

    # Commit the transaction
    cursor.execute("COMMIT")
except Exception as e:
    # Rollback the transaction if an error occurs
    cursor.execute("ROLLBACK")
    print(f"Transaction failed: {str(e)}")
finally:
    cursor.close()
    conn.close()

