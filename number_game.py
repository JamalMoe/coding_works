import random

secret = random.randint(100, 200)
guess = 0
attempts = 0

while guess != secret:
    guess = int(input("Guess your number: "))
    attempts += 1

    if guess > secret:
        print("too high")
    elif guess < secret:
        print("Too low")

print(f"Correct! You got it in {attempts} attempts")