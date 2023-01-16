from validator_collection import validators, checkers, errors

def main():
    email_validity(input("What's your email address? "))

def email_validity(s):
    if checkers.is_email(s):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
