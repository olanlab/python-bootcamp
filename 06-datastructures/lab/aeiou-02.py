sentense = input("Enter your sentense : ")

vowels = { "a" : 0, "e" : 0, "i" : 0, "o" : 0, "u" : 0 }

for x in sentense :
    if (x.lower() in vowels) :
        vowels[x.lower()] += 1
        
print(vowels)