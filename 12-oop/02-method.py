class Human:

    # constructor
    def __init__(self, name = "", age = 0) -> None:
        self.name = name
        self.age = age
    

    # overiding
    def __str__(self) -> str:
        return f"My name is  {self.name}. I am {self.age} years."

    # method
    def eat(self) -> None : 
        print("I can eat!")

    def sleep(self) -> None : 
        print( "I can sleep!")

person = Human()
person.name = "Olan Samritjiarapon"
person.age = 18

print(person)

person.eat()
person.sleep()
person = Human()

print(person.count)

