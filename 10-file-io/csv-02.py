import os 
import csv

try :
    f = open("students.csv", "at", newline="")
    writer = csv.writer(f)

    # writer.writerow(["name", "sex", "gpa"])
    # writer.writerow(["Olan", "M", 3.2])
    # writer.writerow(["Mane", "M", 3.5])
    
    # lists = []
    # lists.append(["name", "sex", "gpa"])
    # lists.append(["Olan", "M", 3.2])
    # lists.append(["Mane", "M", 3.5])
    # lists.append(["Manee", "F", 2.5])
    # writer.writerows(lists)

    for i in range(2) : 
        name = input("name = ")
        sex = input("sex = ")
        gpa = input("gpa = ")
        writer.writerow([name, sex, gpa])



except Exception as e : 
    print(e)
finally : 
    if 'f' in locals() :
        f.close()