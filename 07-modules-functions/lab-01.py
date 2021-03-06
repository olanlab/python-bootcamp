def drawLine(number) : 
    i = 1
    while i <= number :
        print("$", end = "")
        i += 1
    print("")

def drawSquare(number) :
    for i in range(1, (number + 1), 1) :
        for j in range(1, (number + 1), 1) :
            print("*", end = "")
        print("")

def drawTriangle(number) :
    for i in range(1, (number + 1), 1) :
        for j in range(1, (i + 1), 1) :
            print("*", end = "")
        print("")

number = int(input("Enter your number : "))

drawLine(number)
print('----------------------------')
drawSquare(number)
print('----------------------------')
drawTriangle(number)
