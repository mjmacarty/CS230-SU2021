# reaction time tester

import time

print("Welcome to the reaction time tester!")
start_time = time.time()
print("Hit the enter key as fast as you can.")
input()
elapsed_time = time.time() - start_time
print("Wow, that was fast. It took " + str(elapsed_time) + " seconds")
