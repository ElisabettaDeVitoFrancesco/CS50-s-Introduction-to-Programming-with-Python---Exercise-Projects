import random
import sys

def main():
    # Call for the function get level n
    random_int = get_level_n()


     # Conditions of the random integer related to the guessed number
    while True:
        # Call the function get_random integer
        guess_random_int = get_guess()

        if guess_random_int >= 0:

            if guess_random_int < random_int: # If the guessed nr is < random nr print that it's too small and call the function to guess again
                print("Too small!")

            elif guess_random_int > random_int: # If the guessed nr is > random nr print that it's too large and call the function to guess again
                print("Too large!")

            else:
                sys.exit("Just right!")
                #break # Goes out of the while loop only when there is a break, otherwise after each conditions it goes back up to the 1st line after the while

def get_level_n():
    while True:
        try:
            level_n = int(input("Level: "))
            if level_n > 0:
                random_int = random.choice(range(1, level_n+1))
                break # Put the break where all the statements are fullfilled,
                      # otherwise if break at the end and the if condition not met, there is no return value to return
                      # Alternatively, I could have put the 'return ...' here, without the break
        # If the input level n is not a positive integer, prompt again another input
        except ValueError:
            pass

    return random_int

def get_guess():
    while True:
        try:
            guess_random_int = int(input("Guess: "))

            # If the guessed nr is an int return this value

        except ValueError:
            pass
        else:
            break
    return guess_random_int


main()
###################################################################
#level_n = int(input("Level: "))

# If the input level n is not a positive integer, prompt again another input
#if level_n < 0 and type(level_n) != int:
#    level_n = input("Level: ")
    # or try: int(input()) ValueError
# Otherwise, randomly genetare a number between 1 and level n
#else:
#    random_int = random.choice(range(level_n))

# Guess the random int
#guess_random_int = int(input("Guess: "))

#if guess_random_int < 0 and type(guess_random_int) != int:
#    guess_random_int = int(input("Guess: "))
#elif guess_random_int < random_int:
#    print("Too small!")
#    guess_random_int = int(input("Guess: "))
#elif guess_random_int > random_int:
#    print("Too large!")
#    guess_random_int = int(input("Guess: "))
#else:
#    print("Just right!")
