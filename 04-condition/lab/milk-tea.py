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
