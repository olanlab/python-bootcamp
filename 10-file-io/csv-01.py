import os 
import csv

try :
    f = open("students.csv", "rt")

    # reader = csv.DictReader(f, delimiter = ",", skipinitialspace=True)

    # for row in reader : 
    #     print(row.get('gpa'))

    reader = csv.reader(f, delimiter = ",", skipinitialspace=True)

    for row in reader : 
        print(row)

except Exception as e : 
    print(e)
finally : 
    if 'f' in locals() :
        f.close()