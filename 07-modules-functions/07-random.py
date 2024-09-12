import random

print(random.random()) # 0.0 - 1.0
print(random.randint(0, 9)) # 0 - 9 
print(random.randrange(11)) # 0 - 10
print(random.uniform(2.5, 10.0)) # 2.5 - 10.0

print(random.choice(["win", "lose", "draw"])) # single random element from list

print(random.choices(["win", "lose", "draw"], k = 2)) # multi random element from list - with replacement
print(random.sample(["win", "lose", "draw"], k = 2)) # multi random element from list - without replacement

deck = ["ace", "two", "three", "four"]
print("Before shuffle : " + str(deck))
random.shuffle(deck)
print("After shuffle : " + str(deck))

