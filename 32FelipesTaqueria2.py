def main():
    prices = []
    prices = get_input(prices)

    print("Total: $", prices)

def get_input(prices):

    while True:
        try:
            item = input("Item: ").title()

            prices.append(menu[item])

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

#######################################################################################################
def main():
    items = []
    items = get_input(items)

    for i in range(len(items)-1):
        total = menu[items[i]] + menu[items[i+1]] # wrong because sums only two, I need to sum all
        print("\nTotal: $", total)



def get_input(items):

    while True:
        try:
            item = input("Item: ").title()
            items.append(item)
        except EOFError:
            break

    return items

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
