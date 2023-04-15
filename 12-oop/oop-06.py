# Polymorphism

from classes.Employee import Employee
from classes.Employee import CommissionEmployee
from classes.Employee import MonthlyEmployee
from classes.Employee import SaleEmployee

seen = MonthlyEmployee("Seen", 15, "seen@olanlab.com", 30000)
olan = CommissionEmployee("Olan", 20, "olan@olanlab.com", 1000)
new = SaleEmployee("New", 30, "new@gmail.com", 30000, 3000)

for person in (olan, seen, new):
    print(f"{person} | {type(person)}" )
    print(person.getIncome())