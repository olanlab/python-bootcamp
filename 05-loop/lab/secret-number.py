import random

secret_number = random.randint(1, 10)
guess = 0
tries = 0 

while guess != secret_number:
    guess = int(input("Guess the number between 1 and 10 : "))
    tries += 1

    if guess < secret_number:
        print("Your guess is too low")
    elif guess > secret_number:
        print("Your guess is too high")
    
print("You guessed the number in {} tries".format(tries))