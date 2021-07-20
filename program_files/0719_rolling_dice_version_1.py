from random import randint

print("Welcome to the dice roll simulator")
print("How many rolls would you like to try?")
iterations = int(input())

twos = 0
threes = 0
fours = 0
fives = 0
six = 0
seven = 0
eight = 0
nine = 0
ten = 0
eleven = 0
twelve = 0

for iteration in range(iterations):
    roll = randint(1,6) + randint(1,6)

    if roll == 2:
        twos += 1
    elif roll == 3:
        threes += 1
    elif roll == 4:
        fours += 1
    elif roll == 5:
        fives += 1
    elif roll == 6:
        six += 1
    elif roll == 7:
        seven += 1
    elif roll == 8:
        eight += 1
    elif roll == 9:
        nine += 1
    elif roll == 10:
        ten += 1
    elif roll == 11:
        eleven += 1
    elif roll == 12:
        twelve += 1
print(f"2:  {twos * '|'}")
print(f"3:  {threes* '|'}")
print(f"4:  {fours* '|'}")
print(f"5:  {fives* '|'}")
print(f"6:  {six* '|'}")
print(f"7:  {seven* '|'}")
print(f"8:  {eight* '|'}")
print(f"9:  {nine* '|'}")
print(f"10: {ten* '|'}")
print(f"11: {eleven* '|'}")
print(f"12: {twelve* '|'}")