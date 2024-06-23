
command = input("command ( q = exit, o = order, s = show income) = ")
glasses = 0
total = 0

while command != "q":
    if command == "s":
        f = open("daily-income.txt", "rt")
        print(f.read(), end='')
        f.close()
    elif command == "o": 
        size = input("Size = ")
        bubble = input("Add bubble = ")
        ownGlass = input("Own glass = ")

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

f = open("daily-income.txt", "wt")
f.write("You have %d glasses\n" % glasses)
f.write("Your total is : %d THB\n" % total)

f.close()