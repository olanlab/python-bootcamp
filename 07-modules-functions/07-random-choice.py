from random import randint, choice, choices

print(randint(0, 9)) # 0 - 9 
print(choice(["win", "lose", "draw"])) # single random element from list
print(choices(["win", "lose", "draw"], k=2)) # single random element from list
