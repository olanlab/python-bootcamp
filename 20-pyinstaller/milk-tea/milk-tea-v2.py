import csv
import datetime
import os
import sys


if getattr(sys, 'frozen', False):
     extDataDir = sys._MEIPASS
     extDataDir  = os.path.join(extDataDir, 'daily-income.csv')      
else:
     extDataDir = os.getcwd()
     extDataDir = os.path.join(extDataDir, 'daily-income.csv') 
print(f"path of extDataDir is {extDataDir}")

command = input("command ( q = exit, o = order, s = show income) = ")
glasses = 0
total = 0

while command != "q":
    if command == "s":
        f = open(extDataDir, "rt", newline="")
        reader = csv.DictReader(f, fieldnames=["date", "glass", "total"])
        for i, row in enumerate(reader):
            if i != 0:
                print(f"{row['date']}\t{row['glass']}\t{row['total']}")
            else : 
                print(f"{row['date']}\t\t{row['glass']}\t{row['total']}")

                
    elif command == "o": 
        size = input("size = ")
        bubble = input("add bubble = ")
        ownGlass = input("own glass = ")

        price = 0
        if ( size == "M") :
            price += 65
            if (bubble == "Y") :
                price += 10
        elif ( size == "L") :
            price += 80
            if (bubble == "Y") :
                price += 15

        if ( ownGlass == "Y" ) :
            price -= 5

        print("Your bill is : %d THB" % price)
        glasses += 1
        total += price
    command = input("command ( q = exit, o = order, s = show income ) = ")


print("You have %d glasses" % glasses)
print("Your total is : %d THB" % total)


if(os.path.exists("daily-income.csv")):
    f = open("daily-income.csv", "at", newline="")
    writer = csv.DictWriter(f, fieldnames=["date", "glass", "total"])
    writer.writerow({"date": datetime.date.today(), "glass": glasses, "total": total})
else :
    f = open("daily-income.csv", "wt", newline="")
    writer = csv.DictWriter(f, fieldnames=["date", "glass", "total"])
    writer.writeheader()
    writer.writerow({"date": datetime.date.today(), "glass": glasses, "total": total})

f.close()