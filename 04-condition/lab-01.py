x = int(input("Enter your number x : "))
y = int(input("Enter your number y : "))
z = int(input("Enter your number z : "))

print("x = %d, y = %d, z = %d" % (x, y, z) )

if x > y :
    if x > z:
        print(x)
    else :
        print(z)
else:
    if y > z: 
        print(y)
    else:
        print(z)