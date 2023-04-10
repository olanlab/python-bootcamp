number = int(input("Enter your size : "))

for i in range(1, (number + 1), 1) :
    for j in range(1, (i + 1), 1) :
        print("*", end = "")
    print("")