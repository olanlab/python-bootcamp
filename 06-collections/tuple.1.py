tuple1 = ("mini cooper", "honda", "honda", "toyota")
print(tuple1)

print(tuple1[1])
print(len(tuple1))
print(tuple1.count("honda"))
print(tuple1.index("toyota"))

for x in tuple1:
  print(x)

if "honda" in tuple1:
  print("Yes, 'honda' is in the tuple1")