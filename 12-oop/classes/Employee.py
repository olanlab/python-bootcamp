from classes.Human import Human

# derived class
class Employee(Human):

    def __init__(self, name, age, email) -> None:
        super().__init__(name, age)
        self.__email = email 
    
    # Setter
    def setEmail(self, email): 
        self.__email = email

    # Getter
    def getEmail(self):
        return self.__email

    def getIncome(self):
        pass

class MonthlyEmployee(Employee):
    def __init__(self, name, age, email, salary) -> None:
        super().__init__(name, age, email)
        self.__salary = salary
        
    # Setter
    def setSalary(self, email): 
        self.__email = email

    # Getter
    def getEmail(self):
        return self.__email
    
    def getSalary(self): 
        return self.__salary

    def getIncome(self):
        return self.__salary


class SaleEmployee(MonthlyEmployee):
    def __init__(self, name, age, email, salary, commission) -> None:
        super().__init__(name, age, email, salary)
        self.__commission = commission
    
    # Setter
    def setCommission(self, commission): 
        self.__commission = commission

    # Getter
    def getCommission(self):
        return self.__commission

    def getIncome(self):
         return self.getSalary() + self.__commission

class HourlyEmployee(Employee):
    pass


class FreelanceEmployee(HourlyEmployee):
    pass



    






