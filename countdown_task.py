import time

seconds = int(input("count from? "))

for i in range(seconds, 0, -2):
    print(i)
    time.sleep(2)

print("time is up!!!")