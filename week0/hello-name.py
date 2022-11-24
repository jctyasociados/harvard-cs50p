# ask user for the name
name = input("what's your name? ")

# Remove first and last whitespaces from str
name = name.strip()

# Capitalize user name first letter
name = name.capitalize()

# Capitalize all first characters
name = name.title()

# Print hello to user name
print("Hello, " + name)

# Another way of handling variables
print("Hello,", name)

# Another way
print("Hello, ", end="")
print(name)

# Using string formatting
print (f"Hello, {name}")

# ask user for the name and capitalize name and surname
print("Capitalize name and surname.")
name2 = input("what's your name? ").strip().title()

print(f"Hello, {name2}")

# Split name2 into two varibles
first, last = name2.split(" ")

print(f"Hello, {first} {last}")

print("Hello using fuctions")

def hello(to="world"):
	print("Hello,", to)

hello()
name = input("What's your name? ")
hello(name)
