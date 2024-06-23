# my_sql_module.py

import mysql.connector
from mysql.connector import Error


class MySQLConnection:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
            )
            if self.connection.is_connected():
                print("Successfully connected to the database")
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            self.connection = None

    def disconnect(self):
        if self.connection is not None and self.connection.is_connected():
            self.connection.close()
            print("Database connection closed")

    def execute_query(self, query, params=None):
        if self.connection is None or not self.connection.is_connected():
            print("Not connected to the database")
            return None

        cursor = self.connection.cursor()
        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            print("Query executed successfully")
            return cursor.fetchall()
        except Error as e:
            print(f"Error while executing query: {e}")
            return None
        finally:
            cursor.close()

    def execute_update(self, query, params=None):
        if self.connection is None or not self.connection.is_connected():
            print("Not connected to the database")
            return False

        cursor = self.connection.cursor()
        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.connection.commit()
            print("Update executed successfully")
            return cursor.rowcount
        except Error as e:
            print(f"Error while executing update: {e}")
            return cursor.rowcount
        finally:
            cursor.close()
