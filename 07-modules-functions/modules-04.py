import datetime

# DATETIME
now = datetime.datetime.now()
print("now = ", now)

a = datetime.datetime(2019, 11, 11, 12, 30, 50)
print("a = ", a)
print("year = ", a.year)
print("month = ", a.month)
print("day = ", a.day)
print("hour = ", a.hour)
print("minute = ", a.minute)
print("second = ", a.second)

# DIFFERENT
dif = now - a 
print("dif = ", dif)
print("days = ", dif.days)
print("seconds = ", dif.seconds)

# FORMAT
print(now)
print(now.strftime("%d/%m/%Y %H:%M:%S"))
print(now.strftime("%a %d %b %Y %H:%M:%S"))