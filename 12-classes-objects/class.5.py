class Student:
    
    room = 'X'

    def __init__(self, name, point):
        self.name = name
        self.point = point
    
    def introduct(self):
        print("Hello my name is " + self.name + ", my point is " + str(self.point))

s1 = Student("Olan Samritjiarapon", 90)
s2 = Student("Jimmy Clever", 100)
print(s1.room)
print(s2.room)
