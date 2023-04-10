# Polymorphism

from classes.Employee import SaleEmployee
from classes.Employee import MonthlyEmployee

seen = MonthlyEmployee("Seen", 15, "seen@olanlab.com", 30000)
olan = SaleEmployee("Olan", 20, "olan@olanlab.com", 20000, 2002)

print(olan.getIncome())
print(seen.getIncome())

for person in (olan, seen):
    print(person.getIncome())
    print(person.isAdult(person.getAge()))

