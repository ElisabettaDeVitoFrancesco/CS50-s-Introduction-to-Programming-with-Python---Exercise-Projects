import re
import sys

def main():
    print(validate(input("IPv4 Address: ").strip()))

def validate(ip):
    # IPv4 must be dot decimal format #.#.#.#
    # with four spots for numbers and three dots
    # '#' must be between [0,255]
    if digits := re.search("^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip):
        if 0 <= int(digits.group(1)) <= 255 and 0 <= int(digits.group(2)) <= 255 and 0 <= int(digits.group(3)) <= 255 and 0 <= int(digits.group(4)) <= 255:
            return True
        else:
            return False
    else:
        return False

    # function must return True or False

if __name__ == "__main__":
    main()
