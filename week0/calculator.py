x = int(input("What's x? "))
y = int(input("What's y? "))

print(x + y)

print("sum float")
x = float(input("What's x? "))
y = float(input("What's y? "))

print(x + y)

print("sum float with thousands symbol")
x = float(input("What's x? "))
y = float(input("What's y? "))

# Round to nearest integer function: round(number [, ndigits])
z = round(x + y)

print(f"{z:,}")

# Division rounded to two decimals
print("Division with thousands symbol rounded to two decimal points")
x = float(input("What's x? "))
y = float(input("What's y? "))

z = round( x/y, 2)

print(f"{z:,}")