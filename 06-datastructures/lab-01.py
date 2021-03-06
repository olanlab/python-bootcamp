sentense = input("Enter your sentense : ")

a = 0
e = 0
i = 0 
o = 0 
u = 0 

for x in sentense :
    if x == "a" or x == "A" :
        a += 1 
    elif x == "e" or x == "E" :
        e += 1
    elif x == "i" or x == "I" :
        i += 1
    elif x == "o" or x == "O" :
        o += 1
    elif x == "u" or x == "U" :
        u += 1   

print("a=%d ,e=%d, i=%d, o=%d, u=%d" % (a, e, i ,o, u))