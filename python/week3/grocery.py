groceries = []
while True:
    try:
        item = input()
        groceries.append(item.upper())
    except EOFError:
        break

    for item in sorted(set(groceries)):
        print(item)
        