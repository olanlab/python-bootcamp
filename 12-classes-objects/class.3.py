class Student:
    def __init__(self, name, point):
        self.name = name
        self.point = point
    
    def introduct(self):
        print("Hello my name is " + self.name + ", my point is " + str(self.point))

s1 = Student("Olan Samritjiarapon", 90)
print(s1.name)
print(s1.point)
s1.introduct()