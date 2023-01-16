def main():
    money_owed = 50
    print("Amoun due: ", money_owed)
    while money_owed > 0:
        money_owed = insert_coin(money_owed)
    if money_owed <= 0:
        print("Change owed: ", money_owed)

def insert_coin(owed):
    coin = int(input("Insert coin: "))
    if coin == 25 or coin == 10 or coin == 5:
        owed = owed - coin
    print("Amount due: ", owed)
    return(owed)


main()
