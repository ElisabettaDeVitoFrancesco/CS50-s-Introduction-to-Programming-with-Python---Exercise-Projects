import random

def main():
    level_n = get_level()

    for i in range(10):
        x, y = generate_integer(level_n)
        z = x + y
        while True:
                result_input = int(input(f"{x} + {y} = "))

                if result_input == z:
                    score = i + 1
                    break
                elif result_input != z:
                    print("EEE")
                    if result_input != z:
                        print("EEE")
                        if result_input != z:
                            print("EEE")
                            print(f"{result_input}{z}")
                            break
#                else:
#                    for j in range(3):
#                        if j <= 2:
#                            print("EEE")
#                        else:
#                            print(f"{result_input}{z}")
#                            break
#                output = EEE printed 3x consequently and prompt the same problem, over and over again (infinite loop)

    print("Score: ", score)


def get_level():
    # Ask for an input level n
    # If the level n is not 1 nor 2 nor 3, prompt again
    while True:
        try:
            level_n = int(input("Level: "))
            if level_n in [1, 2, 3]:
                return level_n
        except ValueError:
            pass


def generate_integer(level):
    # x = random.randint(10**(level-1), 10**level - 1)
    # y = random.randint(10**(level-1), 10**level - 1)
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)

    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)

    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)

    return x, y



if __name__ == "__main__":
    main()
