point = int(input("Enter your point : "))
grade = float(input("Enter your grade : "))

print("Your point is %d. Your grade is %.2f." % (point, grade))

pointString = str(point)
gradeString = str(grade)
print("Your point is %s. Your grade is %s." % (pointString, gradeString))

print(type(point))
print(type(grade))
print(type(pointString))