x , y = input("Enter the width and height of a rectangle (e.g. 4.0 5.0) : ").split()

area = float(x) * float(y)
perimeter =  float(x) * 2 +  float(y) * 2

print("The rectangle has an area of %.2f sq.unit and %.2f of perimter lenght." % (area, perimeter))

