expression = input("Expression:")
x, operator, y = expression.split(" ")
x = float(x)
y = float(y)   
if operator == "+":
    print(f"{x + y:.1f}")
elif operator == "-":
    print(f"{x - y:.1f}")
elif operator == "*":
    print(f"{x * y:.1f}")
elif operator == "/":
    print(f"{x / y:.1f}")