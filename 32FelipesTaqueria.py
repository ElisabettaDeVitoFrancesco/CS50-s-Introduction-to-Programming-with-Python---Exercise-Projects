def main():
    prices = 0.
    prices = get_input(prices)



def get_input(prices):

    while True:
        try:
            item = input("Item: ").title()

            prices += menu[item] # not a list of items, but a list of integers
            print("Total: $%.2f"% prices)

        except KeyError:
            pass # where does this break?
        except EOFError:
            break

    return prices

menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

main()
