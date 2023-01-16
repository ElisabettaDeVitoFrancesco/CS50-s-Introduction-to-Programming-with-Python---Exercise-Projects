import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    # Count nr of time that um is in the input
    # case-insensitively
    # "um" only as single word not inside other words (e.g. not "yummy", but "I see, um, a tree")
    #
    if um := re.findall(r"\bum\b", s, re.IGNORECASE):
        # print(len(um))
        #print(type(um))
        #counts_um = len(um)

        return int(len(um))

    else:
        return 0


if __name__ == "__main__":
    main()
