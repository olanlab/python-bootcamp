points = []
numbers = int(input("Enter number of students : "))

i = 1
while i < (numbers + 1) :
    try :
        point = int(input("Enter point of student %d : " % i))
        if (point < 0 or point > 100) :
            raise Exception()
    except :
        print("Point is wrong number. please try again.")
        continue
    points.append(point)
    i += 1

# print(points)
i = 1
for j in points :
    if (j >= 80 and j <= 100) :
        print("Student %d - Grade A" % i)
    elif (j >= 70 and j <= 79) :
        print("Student %d - Grade B" % i)
    elif (j >= 60 and j <= 69) :
        print("Student %d - Grade C" % i)
    elif (j >= 50 and j <= 59) :
        print("Student %d - Grade D" % i)
    else : 
        print("Student %d - Grade F" % i)
    i += 1

