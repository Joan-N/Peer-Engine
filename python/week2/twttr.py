text = input("input: ")
result = ""
for char in text:
    if char not in "aeiouAEIOU":
        result += char
print(result)
