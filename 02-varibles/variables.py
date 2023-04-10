import random

ans = random.randint(1, 10)
num = 0

while num != ans:
    num = int(input("Enter answer : "))
    if num > ans:
        print("Too high")
    elif num < ans:
        print("Too low")
    else:
        print("Correct")
    