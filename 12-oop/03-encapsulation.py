class Human:
    # constructor
    def __init__(self, name = "",  age = 0) -> None:
        # public 
        self.name = name
        # private
        self.__age = age

    # overiding
    def __str__(self) -> str:
        return f"My name is  {self.name}. I am {self.__age} years."

    # Setter
    def setAge(self, age) :
        if age < 0 :
            self.__age = 15
        elif age > 100 :
            self.__age = 80
        else :
            self.__age = age
        

    # Getter
    def getAge(self) :
        return self.__age

    # method
    def eat(self) -> None : 
        print("I can eat!")

    def sleep(self) -> None : 
        print( "I can sleep!")

person = Human("Olan Samritjiarapon", 18)

person.setAge(100)
print(person.getAge())
print(person)
