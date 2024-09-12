import mysql.connector
from mysql.connector import errorcode

connection = None
cursor = None

try: 
    connection = mysql.connector.connect(user='root', password='', host='localhost', charset="utf8mb4",  database="shopper" )
    cursor = connection.cursor()

except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("username or password is incorrect")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database doesn't exist")
  else:
    print(err)
finally:
    if cursor != None:
      cursor.close()
    if connection != None:
      connection.close()

  

