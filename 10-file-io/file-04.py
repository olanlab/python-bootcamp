import os 

try :
    f = open("demo2.txt", "rt")
    print(f.read())

    # ERROR
    # number = 10 / 0
    print("************")

    
except FileNotFoundError :
    print("demo.txt is not exist.")
except FileExistsError :
    print("demo.txt is exist.")
except Exception as e : 
    print(e)
finally : 
    if 'f' in locals() :
        f.close()
        print("File is already closed.")