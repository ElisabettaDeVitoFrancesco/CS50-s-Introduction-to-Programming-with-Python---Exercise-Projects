import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # input is a string, s
    # accepted:   9:00 AM to 5:00 PM    or    9 AM to 5 PM     or     9 AM to 5:30 PM    or    5 PM to 9 AM
    # not accepted: 12:60 AM or 13:00 PM or 9 AM - 5 PM or anything else
    # convert to 24h format: 09:00 to 17:00

    working_time = re.search(r"^(\d\d*):?(\d\d|None)?\s(AM|PM)\s(to)\s(\d\d*):?(\d\d|None)?\s(AM|PM)$", s)
    # .group()                     1         2            3       4       5         6           7
    # groups()[]                   0         1            2       3       4         5           6

    if not working_time: raise ValueError

    if int(working_time.group(1)) > 12 or int(working_time.group(5)) > 12: raise ValueError
    if working_time.group(2) != None and int(working_time.group(2)) > 59:  raise ValueError
    if working_time.group(6) != None and int(working_time.group(6)) > 59:  raise ValueError

    time_from = get_24h_format(working_time.group(1), working_time.group(2), working_time.group(3))
    time_to   = get_24h_format(working_time.group(5), working_time.group(6), working_time.group(7))
    new_format_time = time_from + " to " + time_to

    return new_format_time.strip()


def get_24h_format(hours, minutes, AM_PM):

    # add 12 hours unless it's 12 PM
    if AM_PM == "PM": hours = int(hours) + 12 if int(hours) < 12 else 12

    # we actually don't need to change anything for AM unless it's 12
    elif AM_PM == "AM" and int(hours) == 12: hours = 0

    if minutes == None: minutes = "00"
    return f"{int(hours):02}" + ":" + minutes

"""
def get_24h_format(hours, minutes, AM_PM):

    if AM_PM == "PM":
        hours = int(hours) + 12
        if hours == 24:
            hours = 12

    elif AM_PM == "AM":
        hours = int(hours)
        if hours == 12:
            hours = 0

    if minutes == None:
        minutes = "00"
    new_time = f"{hours:02}" + ":" + minutes

    return new_time
"""


if __name__ == "__main__":
    main()
