from databaseUtil import MySQLConnection
import datetime

# Database connection details
host = "localhost"
database = "python"
user = "root"
password = ""


# Initialize connection
db_connection = MySQLConnection(host, database, user, password)

# Connect to the database
db_connection.connect()

# execute_query
query = "SELECT * FROM milkteas"
results = db_connection.execute_query(query)

# Print results
if results:
    for row in results:
        print(row)

# # execute_update
# query = "INSERT INTO milkteas (created_date, glass, total) VALUES ( %s, %s, %s)"
# val = (datetime.date.today(), 1, 60)
# results = db_connection.execute_update(query , val)

# print(results)

# Disconnect from the database
db_connection.disconnect()
