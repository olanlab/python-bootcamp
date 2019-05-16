import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", passwd="goodtime", database="shopper")
cursor = db.cursor()

# sql = "INSERT INTO customers (name, age) VALUES (%s, %s)"
# values = ("Olan Samritjiarapon", 34)
# cursor.execute(sql, values)

sql = "INSERT INTO customers (name, age) VALUES (%s, %s)"
values = [
  ('Olan Samritjiarapon', 34),
  ('Johny JJ', 25),
  ('Jame Marugo', 40),
  ('Saha Nono', 33)
]

cursor.executemany(sql, values)
db.commit()
print(cursor.rowcount, "record inserted.")