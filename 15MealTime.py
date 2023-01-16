# Ask for what time it is to the user
def main ():
    time = input("What time is it? ")
    time_dec = convert(time) # Assign the result of the function to a variable which is the output of the function

    if time_dec >= 7.0 and time_dec <= 8.0:
        print("breakfast time")
    elif time_dec >= 12.0 and time_dec <= 13.0:
        print("lunch time")
    elif time_dec >= 18.0 and time_dec <= 19.0:
        print("dinner time")

# Split and convert the str time into int
def convert(time):
    if time.split(" ")[-1] == "p.m.":
        hours = float(time.split(":")[0]) + 12
        minutes = float(time.split(":")[1].split(" ")[0])/60
    elif time.split(" ")[-1] == "a.m.":
        hours = float(time.split(":")[0])
        minutes = float(time.split(":")[1].split(" ")[0])/60
    else:
        hours = float(time.split(":")[0])
        minutes = float(time.split(":")[1])/60
    time_dec = hours + minutes
    return(time_dec)

if __name__ == "__main__":
    main()
