bill = float(input("How much was the bill? $"))
percent = float(input("What percentage would you like to tip? "))
tip = bill * (percent / 100)
print(f"Leave ${tip:.2f}")

