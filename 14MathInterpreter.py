# Ask the user for the expression to be calculated
expression = input("What do you want to calculate?\nPlease insert spaces between the math symbol. ")

# Split the expression into x as int, y as math symbol, z as int
x = float(expression.split(" ")[0])

y = expression.split(" ")[1]

z = float(expression.split(" ")[2])

# Output the result
if y == "+":
    result = x + z
    print(result)
elif y == "-":
    result = x - z
    print(result)
elif y == "*":
    result = x * z
    print(result)
elif y == "/":
    result = x / z
    print(result)
