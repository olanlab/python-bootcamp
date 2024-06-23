number = int(input("Enter your number : "))

for i in range(2, (number + 1), 1) :
    for j in range(2, i, 1) :
        if (i % j == 0) :
            break
    else : 
        print(str(i) + " ", end = "")
        