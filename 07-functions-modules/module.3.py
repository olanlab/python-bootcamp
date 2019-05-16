import datetime

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))

y = datetime.datetime(2020, 5, 17)
print(y)
print(y.strftime("%d %B %Y %H:%M:%S"))