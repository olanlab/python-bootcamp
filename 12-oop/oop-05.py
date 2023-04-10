# Inheritance

from classes.Human import Human
from classes.Student import Student

# Create object of base class
person = Human("Ken", 20)
print(person)
person.eat()
person.sleep()

# Create object of derived class
stu = Student("olan", 18, "olan@olanlab.com", 3.5)
print(stu)
stu.eat()
stu.sleep()

print(f"Nunber of Objects = {stu.count}")