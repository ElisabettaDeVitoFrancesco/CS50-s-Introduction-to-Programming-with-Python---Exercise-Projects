def main():
    m = int(input("What's your weight in kg? "))
    joule(m)

def joule(m):
    c = 300000000
    csquare = c**2
    E = m * csquare
    print("Your weight in Joules is: ", E)

main()
