import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", passwd="goodtime", database="shopper")
cursor = db.cursor()

cursor.execute("CREATE TABLE customers (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(255), age INT, PRIMARY KEY (id))")