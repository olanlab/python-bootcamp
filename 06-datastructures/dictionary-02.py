dict = {
    "a" : 0, "e" : 0, "i" : 0, "o" : 0, "u" : 0
}

sentense = input("Enter sentense : ")
for x in sentense :
    if x == "a":
        dict["a"] += 1
    elif x == "e":
        dict["e"] += 1
    elif x == "i":
        dict["i"] += 1
    elif x == "o":
        dict["o"] += 1
    elif x == "u":
        dict["u"] += 1

print(dict)





# for x in dict :
#     print(x)

# for x in dict :
#     print(dict[x])

# for x in dict.values() :
#     print(x)

# for x , y in dict.items() :
#     print(x , y)