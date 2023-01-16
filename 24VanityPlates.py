def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W" "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = [".", ",", ":", ";", " ", "!", "?"]

def is_valid(s):
    # min 2 characters max 6 characters

    if len(s) < 2 or len(s) > 6:
        #print('return 1')
        return False

    # Must start with at least 2 letters
    for c in s[0:2]:
        if c not in alphabet:
            #print('return 2')
            return False

    # numbers only at the end, not in the middle
    # if there are numbers, characters afterwards must be numbers too, not alphabet
    for i in range(len(s)-1):
        if s[i] in numbers:
            if s[i+1] in alphabet:
                #print("Return 3")
                return False

#    if len(s) == 4:
#        if s[2] in numbers:
#            if s[3] in alphabet:
#                print('return 3')
#                return False

#    if len(s) == 5:
#        if s[2] in numbers or s[3] in numbers:
#            if s[3] in alphabet or s[4] in alphabet:
#                print('return 4')
#                return False

#    if len(s) == 6:
#        if s[2] in numbers or s[3] in numbers or s[4] in numbers:
#            if s[3] in alphabet or s[4] in alphabet or s[5] in alphabet:
#                print('return 5') # Problem!!!
#                return False

    # first number != 0
    if len(s) == 3 or len(s) == 4:
        if s.find("0") == 2:
            #print('return 6')
            return False

    elif len(s) == 5:
        if s.find("0") == 2 or s.find("0") == 3:
            #print('return 7')
            return False

    elif len(s) == 6:
        if s.find("0") == 2 or s.find("0") == 3 or s.find("0") == 4:
            #print('return 8')
            return False

    # NO . , : ; ! ? " "
    for c in s:
        if c in symbols:
            #print('return 9')
            return False

    return True

main()
