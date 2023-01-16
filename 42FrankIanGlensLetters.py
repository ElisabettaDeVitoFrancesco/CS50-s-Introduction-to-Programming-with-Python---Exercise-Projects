import random
import sys
from pyfiglet import Figlet
figlet = Figlet()

font_list = figlet.getFonts()
#print(font_list)

if len(sys.argv) < 2:
    text_input = input("Input: ")
    font_random = random.choice(font_list)
    print(font_random)
    figlet.setFont(font = font_random)
    print(figlet.renderText(text_input))

elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in font_list:
            text_input = input("Input: ")
            figlet.setFont(font = sys.argv[2])
            print(figlet.renderText(text_input))
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

else:
    sys.exit("Invalid usage")
