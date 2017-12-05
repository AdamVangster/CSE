import random

print("Welcome to the Guessing Game!!")
print("The computer will pick a number from 1 to 50 and")
print("you will have to guess what it is.")
print("Ready")
print("Set")
print("Guess")

# REMEMBER, INPUTS FROM USERS ARE ALWAYS (!!!)
# OF TYPE STRING!!!!

# 1. Generate a number
# 2. Ask the user for an input(number)
# 3. Does the guess match the number
# 4. Add "Higher" amd "Lower"
# 5. Add 5 guess


correct_answer = (random.randint(1, 3))

user_guess = correct_answer

user_guess(input(" "))

def user_guess(correct_answer):
    user_guess(input(" "))
    if correct_answer >= user_guess:
        print("Lower")
    elif correct_answer <= user_guess:
        print("Higher")


