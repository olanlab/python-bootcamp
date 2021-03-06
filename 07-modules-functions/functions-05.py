def factorial(number) :
    result = 1 
    while number > 0 :
        result = result * number
        number = number - 1
    return result

# print(factorial(0))

def factorialRecursive(number) :
    if number == 1 or number == 0 :
        return 1
    else :
        return number * factorialRecursive(number - 1)

print(factorialRecursive(5))
