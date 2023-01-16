def main():
    emoticonsinput = input("How are you feeling today? ")
    convert(emoticonsinput)

def convert(emoticonsinput):
    emoticonsinput = emoticonsinput.replace(":)", "🙂")
    emoticonsinput = emoticonsinput.replace(":(", "🙁")
    print(emoticonsinput)

main()
