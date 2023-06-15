import mysql.connector

connection = mysql.connector.connect(user='root', host='localhost', charset="utf8mb4",  database="shopper" )

cursor = connection.cursor()
cursor.execute("""CREATE TABLE `customersx` (
  `id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `age` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;""")

# cursor.execute("""ALTER TABLE customersx
# ADD email varchar(255)""")

# cursor.execute("""ALTER TABLE customersx
# DROP email""")

# cursor.execute("""ALTER TABLE customersx
# MODIFY email varchar(500)  NULL """)

# cursor.execute("DROP TABLE customersx")

cursor.close()
connection.close()