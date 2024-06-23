import mysql.connector

connection = mysql.connector.connect(
    user="root", host="localhost", charset="utf8mb4", database="python"
)
cursor = connection.cursor()


def calCulateMean(gpas):
    return sum(gpas) / len(gpas)


def calCulateMedian(gpas):
    sorted_list = sorted(gpas)
    n = len(sorted_list)
    if n % 2 == 0:
        median_value = (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2
    else:
        median_value = sorted_list[n // 2]
    return median_value


def calCulateMode(gpas):
    mode = max = 0
    gpasSet = set(gpas)

    for gpa in gpasSet:
        if max < gpas.count(gpa):
            max = gpas.count(gpa)
            mode = gpa
    return mode


command = ""
fieldnames = ["id", "name", "sex", "gpa"]

while command != "q":
    command = input(
        "command ( q = exit, i = insert, d = delete, s = show, stat = statistic) = "
    )
    # i = insert
    if command == "i":
        firstname = input("firstname : ")
        lastname = input("lastname : ")
        sex = input("sex : ")
        gpa = input("gpa : ")
        sql = "insert into students (firstname, lastname, sex, gpa) values (%s, %s, %s, %s)"
        val = (firstname, lastname, sex, gpa)

        cursor.execute(sql, val)
        connection.commit()
    # d = delete
    elif command == "d":
        id = input("id : ")
        sql = "delete from students where id = %s"
        val = (id,)
        cursor.execute(sql, val)
        connection.commit()
    # s = show, stat = statistic
    elif command == "s" or command == "stat":
        # READ FILE
        if command == "s":
            cursor.execute("select * from students")
            result = cursor.fetchall()
            for row in result:
                print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}")
        elif command == "stat":
            cursor.execute("select gpa from students")
            result = cursor.fetchall()


connection.close()
