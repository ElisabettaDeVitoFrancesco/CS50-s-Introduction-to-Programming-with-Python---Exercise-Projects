plate = input("Plate: ").upper()
#print(plate)
#print(len(plate))
#print(plate[0:2])
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = [".", ",", ":", ";", " ", "!", "?"]

for c in plate[0:2]:
    print(bool(c in alphabet))

print(bool(len(plate) >= 2 and len(plate) <= 6))

print(bool(plate[-1] in numbers))

for c in plate:
    print(bool(c not in symbols))
