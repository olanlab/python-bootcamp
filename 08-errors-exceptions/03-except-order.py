x = int(input("Enter your number : "))


try :
    y = 100 / x
    print(y)
except ZeroDivisionError :
    print("ZeroDivisionError")
except FloatingPointError :
    print("FloatingPointError")
except OverflowError :
    print("OverflowError")
except ArithmeticError :
    print("ArithmeticError")
except : 
    print("Error!!")


