x = int(input("Enter your number : "))

try :
    y = 100 / x
    print(y)
except ZeroDivisionError :
    print("ZeroDivisionError")
