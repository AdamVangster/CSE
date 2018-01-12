import random

print("Welcome to lucky 7's")
print("You will start with 15 dollars and")
print("each round you will bet 1 dollar.")
print("The computer will roll 2 dice and")
print("and if the sum equal to 7, then")
print("you will get your 1 dollar back and")
print("and a additional 4 dollar too.")

your_money = 15
rounds = 0

while your_money > 0:
    D1 = random.randint(1, 6)
    D2 = random.randint(1, 6)
    total = D1 + D2

    if total == 7:
        print("You got your money back and $4 more")
        your_money += 5
        rounds += 1
        print(your_money)
    elif total < 7:
        print("You lost $1")
        rounds += 1
        your_money -= 1
        print(your_money)
    elif total > 7:
        print("You lost $1")
        your_money -= 1
        rounds += 1
        print(your_money)
    if your_money == 0:
        print("You lasted %s rounds" % rounds)



