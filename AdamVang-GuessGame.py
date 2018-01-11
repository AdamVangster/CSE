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
# 4. Add "Higher" and "Lower"
# 5. Add 5 guess
# correct_answer = (random.randint(1, 1))

answer = random.randint(1, 50)
turns_left = 5
correct_guess = False

print(random.randint(1, 1))

while turns_left > 0 and correct_guess is false:
    guess = int(input("guess a number between 1 and 50: "))

    if user_guess == correct_answer:
        return "Correct"
    elif user_guess >= correct_answer:
        return("Higher")
    elif user_guess <= correct_answer:
        return("Lower")
