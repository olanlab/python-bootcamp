def add(*args):

    sum = 0 
    for n in args:
        sum += n
    return sum

print(add(1,2,3))


def calculate(n, **kwargs):
    print(kwargs)
    print(n + kwargs["add"])
    print(n * kwargs["multiply"])

calculate(2, add=3, multiply=5)
