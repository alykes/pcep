import math

x = float(input("Enter x: "))   # any value can be entered here; ValueError
y = math.sqrt(x)                # doesn't check for negative values; ValueError

print("The square root of", x, "equals to", y)