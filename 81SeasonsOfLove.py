from datetime import date
import re
import sys
import inflect

def main():
    # input birthday date yyyy-mm-dd format
    birthday_date = input("Date of birth: ")

    # function to check the correct format of the input birth date
    try:
        birthday_date = format_date(birthday_date)
    except ValueError:
        # if not this format YYYY-MM-DD, exit: sys.exit("Invalid date")
        sys.exit("Invalid date")

    year, month, day = birthday_date.split("-")
    birthday_date = date(int(year), int(month), int(day))

    # Save in variable today's date, with datetime.date.today
    # default time of present day 00:00:00, with strftime().replace()

    # Do not consider the time!!
    #present_date = datetime.now()
    #present_date = present_date.replace(hour = 00, minute = 00, second = 00, microsecond = 00)
    #present_date_str = "2000-01-01 00:00:00"
    #present_date = datetime.strptime(present_date_str, '%Y-%m-%d %H:%M:%S')

    present_date = date.today()
    #present_date_str = "2000-01-01"
    #present_date = date.strptime(present_date_str, '%Y-%m-%d')

    present_year = present_date.year

    # function to calculate the leap years
    delta = delta_leap_dates(present_date, birthday_date)

    # function to calculate the total minutes
    minutes_lived_numbers = date_to_minutes(delta)

    # function to translate minutes from digits to words
    minutes_lived_words = numbers_minute_to_words(minutes_lived_numbers)

    # print it as words
    print(f"{minutes_lived_words} minutes")

def format_date(birthday_date):
    # check if the format of the birthday date is %Y-%m-%d
    if re.search(r"^[\d]{4}-[\d]{2}-[\d]{2}$", birthday_date):
        return birthday_date


def delta_leap_dates(present_date, birthday_date):
    # Do not consider the leap years!!
    #leap_days = round((int(present_year) - int(birthday_date.year)) / 4) # leap_years = days more, then in next function: * 24h * 60min
    delta = present_date - birthday_date

    return delta

def date_to_minutes(delta):
    #leap_minutes = leap_days * 24 * 60

    minutes_lived_numbers = delta.days * 24 * 60

    # minutes_lived_numbers = leap_minutes + delta_minutes

    return minutes_lived_numbers

def numbers_minute_to_words(minutes_lived_numbers):
    inflector = inflect.engine()
    minutes_lived_words = inflector.number_to_words(minutes_lived_numbers, andword="").capitalize()

    return minutes_lived_words

if __name__ == "__main__":
    main()
