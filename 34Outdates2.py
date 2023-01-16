months_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    year, month, day = date_format()
    print(f"{year}-{month:02}-{day:02}")

def date_format():
    global year
    global month
    global day
    while True:
        try:
            date = input("Date: ") # as m/d/yyyy or Month d, yyyy

            if "/" in date:
                if int(date.split("/")[0]) >= 1 and int(date.split("/")[0]) <= 12:
                    month = int(date.split("/")[0])
                if int(date.split("/")[1]) >= 1 and int(date.split("/")[1]) <= 31:
                    day = int(date.split("/")[1])
                year = int(date.split("/")[2])


            elif "," in date:
                if date.split(" ")[0] in months_list:
                    month = months_list.index(date.split(" ")[0]) + 1
                if int(date.split(" ")[1].split(",")[0]) >= 1 and int(date.split(" ")[1].split(",")[0]) <= 31:
                    day = int(date.split(" ")[1].split(",")[0])
                year = int(date.split(",")[1].strip())

            else:
                date = input("Date: ") # as m/d/yyyy or Month d, yyyy

        except NameError:
            pass

        except ValueError:
            pass

        else:
            break
    return year, month, day

main()
#print(months_list.index()==month)


