from abc import ABC, abstractmethod
from classes.Human import Human

# derived class
class Employee(Human, ABC):

    # class variables
    company = "OlanLab Co.,Ltd."
    count = 0

    # class methods
    @classmethod
    def updateCount(cls, value) :
        cls.count += value

    def __init__(self, name, age, email) -> None:
        super().__init__(name, age)
        self.__email = email 
        Employee.updateCount(1)
        
    
    # Setter
    def setEmail(self, email): 
        self.__email = email

    # Getter
    def getEmail(self):
        return self.__email

    @abstractmethod
    def getIncome(self):
        pass

    def __str__(self) -> str:
        return f"{super().__str__()} My email is {self.getEmail()}."

class MonthlyEmployee(Employee):
    def __init__(self, name, age, email, salary = 0) -> None:
        super().__init__(name, age, email)
        self.__salary = salary
        
    # Setter
    def setSalary(self, salary): 
        self.__salary = salary

    # Getter
    def getSalary(self): 
        return self.__salary

    def getIncome(self):
        return f"Salary = {self.getSalary()}."
    
    def __str__(self) -> str:
        return f"{super().__str__()} My salary is {self.getSalary()}"

class CommissionEmployee(Employee):
    def __init__(self, name, age, email, commission = 0) -> None:
        super().__init__(name, age, email)
        self.__commission = commission
    
    # Setter
    def setCommission(self, commission): 
        self.__commission = commission

    # Getter
    def getCommission(self):
        return self.__commission

    def getIncome(self):
          return f"Commission = {self.getCommission()}."
    
    def __str__(self) -> str:
        return f"{super().__str__()} My commission is {self.getCommission()}."


class SaleEmployee(MonthlyEmployee, CommissionEmployee):
    def __init__(self, name, age, email, salary, commission) -> None:
       super().__init__(name, age, email)
       self.setSalary(salary)
       self.setCommission(commission)
    
    # Getter
    def getIncome(self):
         return  f"Salary = {self.getSalary()} and Commission = {self.getCommission()}."

class HourlyEmployee(Employee):
    pass


class FreelanceEmployee(HourlyEmployee):
    pass



    






