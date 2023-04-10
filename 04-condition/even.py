w = int(input("Enter your number w : "))
x = int(input("Enter your number x : "))
y = int(input("Enter your number y : "))
z = int(input("Enter your number z : "))

even = 0

if (w % 2 == 0): 
    even = even + 1

if (x % 2 == 0): 
    even = even + 1

if (y % 2 == 0): 
    even = even + 1

if (z % 2 == 0): 
    even = even + 1

print("จำนวนเลขคู่เท่ากับ %d" % (even))