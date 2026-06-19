greeting = input("Greeting: ").strip().lower()
if greeting == "hello":
    print("$0")
elif "hello" in greeting:
    print("$20")
else:
    print("$100")
