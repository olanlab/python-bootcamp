
PI = 3.14

def calCircleArea(radius) :
    return ( PI * pow(radius, 2))
    
def calSquareArea(length, width) :
    return  length * width 

def calTriangleArea(base, height) :
    return base * height / 2 

print(calSquareArea(10, 5)  + calTriangleArea(10, 20))
print(calCircleArea(10))