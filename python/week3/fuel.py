fraction = input("Fraction: ")
x, y = fraction.split("/")
x = int(x)
y = int(y)
percentage = round(x / y * 100)
if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f"{percentage}%")
    