for x in range(11):
  if (x == 5 or x == 7):
    continue
  print(x)
else:
  print("Finally finished!")

print("#########################")

for x in range(11):
  if (x == 5 or x == 7):
    break
  print(x)
else:
  print("Finally finished!")