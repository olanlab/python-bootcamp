numbers = [1, 2, 3, 4, 5]

dict = {
    "firstname" : "Olan",
    "lastname" : "Samritjiarapon",
    "hp" : 100,
    "mp" : 50
}

try : 
    print(dict['sp'])
except IndexError :
    print("IndexError")
except KeyError :
    print("KeyError")
else : # NO ERROR OR NO EXCEPTION
    print("No Error!!")
finally : 
    print("FINISH!!")
