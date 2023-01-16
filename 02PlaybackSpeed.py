def main():
    textinput = input("Enter your text. ")
    playback(textinput)

def playback(textinput):
    textinput = textinput.replace(" ", "...")
    print(textinput)

main()
