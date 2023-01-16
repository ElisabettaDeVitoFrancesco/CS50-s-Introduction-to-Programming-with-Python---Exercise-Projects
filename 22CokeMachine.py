def main():
    money_owed = 50
    print("Amoun due: ", money_owed)

    while money_owed > 0:
        money_owed = insert_coin(money_owed)
        if money_owed > 0:
            print("Amount due: ", money_owed)
        else:
            print("Change owed: ", money_owed*-1)

def insert_coin(owed):
    coin = int(input("Insert coin: "))
    if coin == 25 or coin == 10 or coin == 5:
        owed = owed - coin

    return(owed)


main()
