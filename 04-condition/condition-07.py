value = 100

if value < 200 : 
    print("value is less than 200")
    if value == 150:
        print("value is 150")
    elif value == 100:
        print("value is 100")
    elif value == 50:
        print("value is 50")
else :
    print("value is equal to 200 or greater than 200.")

print("-----------------------------------------")

if value < 200 and value == 150 : 
    print("value is less than 200")
    print("value is 150")
elif value < 200 and value == 100 : 
    print("value is less than 200")
    print("value is 100")
elif value < 200 and value == 50 : 
    print("value is less than 200")
    print("value is 50")
else : 
    print("value is equal to 200 or greater than 200.")