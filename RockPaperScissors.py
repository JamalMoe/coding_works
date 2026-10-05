import random

options = ["rock", "paper", "scissors"]
beats = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

player = input("choose rock, paper, or scissors: ").lower()
if player in options:

    computer = random.choice(options)

    print(f"computer chose: {computer}")

    if player == computer:
        print("its a tie!")

    elif beats [player] == computer:
        print("you win!")

    else:
        print("you lose")

else:
    print("Wrong choice")