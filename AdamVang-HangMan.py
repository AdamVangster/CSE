import random
# This is a guide of how to
# make hangman
#
# 1. Make a word bank - 10 items
# 2. Select a random item to guess
# 3. Take in a letter and add it to a list of letters_guessed
# 4. Hide and reveal letters
# 5. Create win and lose conditions


word_banks = ['OverWatch', 'League of Legends', 'Fortnite', 'God Staff Jax', 'NightBringer Yasuo', 'God Fist Lee Sin',
              "Cloud9", "Garchomp", "Gardevoir", "Volcarona"]

# for word in word_banks:
#     print(word)

# print(random.choice(Word_Banks))

strOne = random.choice(word_banks)
listOne = strOne
print(listOne)

current_guess = ""
letters_guessed = [' ']
guesses = 11

while guesses > 0:
    output = []
    for letter in strOne:
        if letter.lower() in letters_guessed:
            output.append(letter)
        else:
            output.append("*")
    print(output)

    current_guess = input("Guess A Letter or The Word: ").lower()
    if current_guess not in strOne:
        guesses -= 1
        print("You have %s more guesses." % guesses)
    letters_guessed.append(current_guess)
    print("Letters You Guessed: %s " % letters_guessed)
    if guesses == 0:
        print("You Lose")
    if current_guess == strOne:
        print("Correct")
        "".join(output)
