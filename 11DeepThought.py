# Ask the answer to the Great Question of Life to the user
answer_GQoL = input("What's the answer to the Great Question of Life? ").strip().lower()

if answer_GQoL == "42" or answer_GQoL == "forty-two" or answer_GQoL == "forty two":
    print("Yes")
else:
    print("No")
