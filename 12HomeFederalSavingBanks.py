# Ask fro a greeting from the user
greeting = input("Greeting: ").strip().lower().split(",")[0].split()[0] #case and space independent + check only the first word of the string

# If the greeting is equal to "hello" the output is 0$
if greeting == "hello":
    print("$0")
# If the greeting is equal to anything starting with an "h" except "hello" the output is 20$
elif greeting[0] == "h" and greeting != "hello":
    print("$20")
# If the greeting is anything else the output is 100$
else:
    print("$100")
