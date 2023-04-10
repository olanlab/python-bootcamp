import mysql.connector

connection = mysql.connector.connect(user='root', host='localhost', charset="utf8mb4",  database="shopper" )

cursor = connection.cursor()
cursor.execute("CREATE DATABASE mydatabase")
# cursor.execute("DROP DATABASE mydatabase")

connection.close()