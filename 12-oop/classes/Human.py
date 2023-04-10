class Human:
    
    # class variables
    count = 0
    # class methods
    @classmethod
    def updateCount(cls, value) :
        cls.count += value


    # static methods
    @staticmethod
    def isAdult(age) :
        return age > 18
    
    # constructor
    def __init__(self, name = "",  age = 0) -> None:
        self.__name = name
        self.__age = age
        self.updateCount(1)

    # overiding
    def __str__(self) -> str:
        return f"My name is  {self.__name}. I am {self.__age} years."

    # Setter
    def setAge(self, age) :
        if age < 0 :
            self.__age = 15
        elif age > 100 :
            self.__age = 80
        else :
            self.__age = age

    def setName(self, name) :
        self.__name = name
    
    # Getter
    def getAge(self) :
        return self.__age

    def getName(self) :
        return self.__name

    # method
    def eat(self) -> None : 
        print("I can eat!")

    def sleep(self) -> None : 
        print( "I can sleep!")