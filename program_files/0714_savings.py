# savings calculator

print("Welcome to the savings calculator.")
print("Enter your inital deposit amount...")
print("...and I will tell you how much you have in five years.")

deposit = float(input("Enter inital deposit: "))
r = .015
print(f"{'Year':<10s}{'Balance':>15s}")
print("_" * 25)
for year in range(1,6):
    balance = f"$ {deposit * (1 + r) ** year:.2f}"
    print(f"{year:<10}{balance:>15s}")

