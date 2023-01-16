def main():
    text = str(input("Please, enter your text. "))
    textlow(text)

def textlow(text = "Nothing"):
    text = text.lower()
    print("Your text in lower case is: ", text)

main()
