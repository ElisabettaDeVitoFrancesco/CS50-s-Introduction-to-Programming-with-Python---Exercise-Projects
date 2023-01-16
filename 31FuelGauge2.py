while True:
        try:
            fraction = input("Fraction: ")
            x = int(fraction.split("/")[0])
            y = int(fraction.split("/")[1])

            fuel = round( (x / y) * 100 )

        except ValueError:
            print("Not an integer")

        except ZeroDivisionError:
            print("Y should not be 0")

        else:
            break

if fuel == 99 or fuel == 100:
    print("F")
elif fuel <= 1:
    print("E")
else:
    print(f"{fuel}%")
