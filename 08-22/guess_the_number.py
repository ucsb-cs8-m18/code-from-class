import random

up_to = int(input("What number do you want to guess up to? "))
assert(up_to >= 1)

number = random.randint(1, up_to) # pick a number from 1 to 100
guess = -1

while guess != number:
    guess = int(input("Enter your guess: "))
    
    if guess < number:
        print("Too low")
    elif guess > number:
        print("Too high")
    else:
        print("You got it!")
