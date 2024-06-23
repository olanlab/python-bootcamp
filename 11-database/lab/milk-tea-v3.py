import mysql.connector
import datetime

connection = mysql.connector.connect(
    user="root", host="localhost", charset="utf8mb4", database="python"
)
cursor = connection.cursor()

command = input("command ( q = exit, o = order, s = show income) = ")
glasses = 0
total = 0

while command != "q":
    # SHOW
    if command == "s":
        cursor.execute("select * from milkteas")
        result = cursor.fetchall()
        for row in result:
            print(f"{row[0]}\t{row[1]}\t{row[2]}")

    # ORDER
    elif command == "o":
        size = input("size = ")
        bubble = input("add bubble = ")
        ownGlass = input("own glass = ")

        price = 0
        if size == "M":
            price += 65
            if bubble == "Y":
                price += 10
        elif size == "L":
            price += 80
            if bubble == "Y":
                price += 15

        if ownGlass == "Y":
            price -= 5

        print("Your bill is : %d THB" % price)
        glasses += 1
        total += price
    command = input("command ( q = exit, o = order, s = show income ) = ")

sql = "INSERT INTO milkteas (created_date, glass, total) VALUES ( %s, %s, %s)"
val = (datetime.date.today(), glasses, total)
cursor.execute(sql, val)
connection.commit()

print("You have %d glasses" % glasses)
print("Your total is : %d THB" % total)
