import os

if os.path.exists("demo3.txt"):
  os.remove("demo3.txt")
else:
  print("The file does not exist")