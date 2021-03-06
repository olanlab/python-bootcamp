import datetime

# DATE
today = datetime.date.today()
print("today =", today )
print("year =", today.year )
print("month =", today.month )
print("day =", today.day )

a = datetime.date(2019, 4, 13)
print("a =", a)

# TIME
b = datetime.time()
print("b =", b)

c = datetime.time(11, 34, 56)
print("c =", c)
print("hour =", c.hour)
print("minute =", c.minute)
print("second =", c.second)