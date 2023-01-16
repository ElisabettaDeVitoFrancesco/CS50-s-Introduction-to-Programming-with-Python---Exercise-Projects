import csv
import sys

def main():
    csv_check()
    input_csv = sys.argv[1]
    output_csv = sys.argv[2]
    names_house = first_second_house(input_csv)
    names_house_output(output_csv, names_house)


def csv_check():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].split(".")[1] != "csv" and sys.argv[2].split(".")[1] != "csv":
        sys.exit("Not a CSV file")

def first_second_house(input_csv):
    names_house = []
    try:
        with open(input_csv) as file:
            reader = csv.DictReader(file)

            for row in reader:
                names_house.append({
                    "first" : row["name"].split(",")[1].strip(),
                    "last" : row["name"].split(",")[0].strip(),
                    "house" : row["house"]})
    except FileNotFoundError:
        sys.exit(f"Could not read {input_csv}")
    #print(names_house)
    #print(len(names_house))
    return (names_house)

def names_house_output(output_csv, names_house_list):
    with open(output_csv, "w") as file:
        writer = csv.DictWriter(file, fieldnames = ["first", "last", "house"])
        writer.writeheader()

        for i in range(len(names_house_list)):
            dict_i = names_house_list[i]
            writer.writerow({
                "first" : dict_i["first"],
                "last" : dict_i["last"],
                "house" : dict_i["house"],})




# Error of non existing file
# Missing header in the output csv file

if __name__ == "__main__":
    main()
