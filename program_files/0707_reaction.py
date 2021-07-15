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
start_time = time()
print("Hit the enter key as fast as you can.")
input()
elapsed_time = time() - start_time
print("Wow, that was fast. It took " + str(elapsed_time) + " seconds")
