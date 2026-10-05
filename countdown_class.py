import time

seconds = int(input("Count from? "))

for i in range(seconds, 0, -5):
    print(i)
    time.sleep(5)

print("Time is up!!!!")