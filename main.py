def calculate(x, y, z):
    if x == "add":
        return y + z
    elif x == "subtract":
        return y - z
    elif x == "multiply":
        return y * z
    else:
        return y / 2
print (calculate("subtract", 5, 5))