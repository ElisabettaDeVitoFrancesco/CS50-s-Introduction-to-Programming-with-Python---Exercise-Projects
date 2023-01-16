# Ask for a string input, in camel case
def main():
    camel_case = input("What's the name of the variable in camel case? ")
    snake_case(camel_case)

def snake_case(camel_case):
    for c in camel_case:
        if c.isupper():
            print("_" + c.lower(), end = "")
        else:
            print(c, end = "")
    print()

main()
