import time

input("press enter to start the stopwatch...")
start = time.time()

try:
    input("press enter again to stop...")
except KeyboardInterrupt:
    pass

end = time.time()
elapsed = end - start

print(f"elapsed time: {elapsed:.2f} seconds")
