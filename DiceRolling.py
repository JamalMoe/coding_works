import random

num_dice = int(input("How many dice do you want to roll? "))


results = []

for _ in range(num_dice):
    results.append(random.randint(1, 6))

print("you rolled:", results)
print("total:", sum(results) )