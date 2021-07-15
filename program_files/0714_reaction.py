# reaction time tester
"""
Improvements added:
1. Add randomness to prompt
2. Use time and sleep
3. give the user 5 tries
4. display reaction time with 3 decimals
5. after fifth try display average time
"""

from time import time, sleep
from random import random

print("Welcome to the reaction time tester!")
print("You will have 5 tries to show us your speed")
print("When you see the prompt hit the enter key")
print("Get ready!")
sleep(1)
prompt = 0
total_time = 0
average_time = 0
for attempt in range(5):
    prompt = 5 * random()
    sleep(prompt)
    start_time = time()
    print("Hit the enter key as fast as you can.")
    input()
    elapsed_time = time() - start_time
    # total_time = total_time + elapsed_time
    total_time += elapsed_time
    print(f"Wow, that was fast. It took {elapsed_time:.3f} seconds")

print("=" * 30)
average_time = total_time / (attempt + 1)
print(f"Your average time was {average_time:.3f}")
