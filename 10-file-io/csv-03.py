import os 
import csv

try :
    f = open("students.csv", "at", newline="")
    fieldnames = ["name", "sex", "gpa"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    # writer.writeheader()
    # writer.writerow({'name': 'Olan', 'sex': 'M', 'gpa': 3.2})
    # writer.writerow({'name': 'Mane', 'sex': 'M', 'gpa': 3.5})
    # writer.writerow({'name': 'Manee', 'sex': 'F', 'gpa': 2.5})

    # lists = []
    # lists.append({'name': 'Olan', 'sex': 'M', 'gpa': 3.2})
    # lists.append({'name': 'Mane', 'sex': 'M', 'gpa': 3.5})
    # lists.append({'name': 'Manee', 'sex': 'F', 'gpa': 2.5})
    # lists.append({'name': 'Jane', 'sex': 'F', 'gpa': 1.5})
    # writer.writerows(lists)

    for i in range(2) :
        name = input("name = ")
        sex = input("sex = ")
        gpa = input("gpa = ")
        writer.writerow({'name' : name, 'sex': sex, 'gpa' : gpa})


except Exception as e : 
    print(e)
finally : 
    if 'f' in locals() :
        f.close()