fullname = input("Enter your name : ")
weight = float(input("Enter your weights (kg) : "))
height = float(input("Enter your heights (cm) : "))
bmi = weight / ((height / 100) ** 2)

print("%s.Your bmi is %f" % (fullname, bmi))