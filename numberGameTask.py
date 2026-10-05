import random

secret = random.randint(50, 100)
guess = 0
attempts = 0

while guess != secret:
    guess = int(input("guess a number between 50 and 100: "))
    attempts += 1

    if guess < secret:
        print("too low!")
    elif guess > secret:
        print("too high!")

print(f"correct! you got it in {attempts} attempts.")