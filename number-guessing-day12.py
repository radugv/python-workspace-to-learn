import random

number = random.randint(0,100)

easy_mode = 'easy'
hard_mode = 'hard'

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")
mode = input("Choose a dificulty. Type 'easy' or 'hard'")

if mode == easy_mode: 
    attempts = 10
elif mode == hard_mode:
    attempts = 5
else: attempts =0

you_have_not_found_yet_the_number = True
while you_have_not_found_yet_the_number and attempts > 0:
    guess = int(input("Make a guess: "))

    if number > guess:
        print("Too low.")
        print("Guess again.")
        attempts -= 1
        print(f"You have {attempts} attempts left to guess the number.")
    elif number < guess:
        print("Too high.")
        print("Guess again.")
        attempts -= 1
        print(f"You have {attempts} attempts left to guess the number.")
    else:
        print("You have been chosen.")
        break
