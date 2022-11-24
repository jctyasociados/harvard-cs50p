""" Script that take a string from the user and convert white spaces with three dots """

str_to_replace = input("Enter string to convert white spaces: \n")
str_to_replace = str_to_replace.replace(" ", "...")
print(str_to_replace)