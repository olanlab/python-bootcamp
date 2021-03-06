import os 

f = open("readme.txt", "rt")
# print(f.read())
# print(f.readline(), end = "")
# print(f.readline(), end = "")
# print(f.readline(), end = "")

lines = f.readlines()
# print(lines)

for line in lines :
    print(line, end = "")
