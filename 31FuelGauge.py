def main():

    fuel = get_fuel()

    if fuel == 99 or fuel == 100:
        print("F")
    elif fuel > 100:
        fuel = get_fuel()
    elif fuel <= 1:
        print("E")
    else:
        print(f"{fuel}%")

def get_fuel():
    while True:
        try:
            fraction = input("Fraction: ")
            x = int(fraction.split("/")[0])
            y = int(fraction.split("/")[1])

            fuel = round( (x / y) * 100 )

        except ValueError:
            pass

        except ZeroDivisionError:
            pass

        else:
            break

    return fuel

main()
