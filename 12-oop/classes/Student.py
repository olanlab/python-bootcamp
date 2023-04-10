from classes.Human import Human

# derived class
class Student(Human):

    def __init__(self, name, age, email, grade) -> None:
        super().__init__(name, age)
        self.__email = email 
        self.__grade = grade

    # Getter
    def getEmail(self) :
        return self.__email

    def getGrade(self) :
        return self.__grade

    # Setter
    def setEmail(self, email) :
        self.__email = email

    def setGrade(self, grade) :
        self.__grade = grade

    # overiding 
    def __str__(self) -> str:
        return f"[Student]{super().__str__()}\nEmail : {self.__email}, Grade : {self.__grade}" 