def main():
    complete_input = input("Input: ")
    print("Output: ", end = "")
    remove_vowels(complete_input)
    print("\n", end = "")

def remove_vowels(complete_input):
    for c in complete_input:
        if c in ("a", "A", "e", "E", "i", "I", "o", "O", "u", "U"):
            print(c.replace(c, ""), end = "")
        else:
            print(c, end = "")

main()
