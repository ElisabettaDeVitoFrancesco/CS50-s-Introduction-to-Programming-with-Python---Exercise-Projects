import csv
import sys
from tabulate import tabulate

def main():
    menu_csv_check()
    csv_file = sys.argv[1]
    write_pretty_menu(csv_file)

def menu_csv_check():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].split(".")[1] != "csv":
        sys.exit("Not a CSV file")

def write_pretty_menu(csv_file):
    menu = []
    try:
        with open(csv_file) as file: # Open the input file and save it in file

            if csv_file == "sicilian.csv":
                reader = csv.DictReader(file) # Read the input file, and return it as dictionary

                for row in reader: # For each row of the list (menu)
                    menu.append({"Sicilian Pizza": row["Sicilian Pizza"], # add as a dict, to the keys that I wrote,
                    "Small":row["Small"], "Large":row["Large"]}) # the items of each key

            elif csv_file == "regular.csv":
                reader = csv.DictReader(file) # Read the input file, and return it as dictionary

                for row in reader: # For each row of the list (menu)
                    menu.append({"Regular Pizza": row["Regular Pizza"], # add as a dict, to the keys that I wrote,
                    "Small":row["Small"], "Large":row["Large"]}) # the items of each key

    except FileNotFoundError:
            sys.exit("File does not exist")

    print(tabulate(menu, headers = "keys", tablefmt="grid"))

if __name__ == "__main__":
    main()
