x = -1

try :
    if x < 0 : 
        raise Exception("Sorry, no number below zero") 
except Exception as e :
    print(e)
