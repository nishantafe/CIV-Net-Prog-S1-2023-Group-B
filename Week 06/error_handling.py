# EAFP
# Easier to ask for forgiveness than permission

# LBYL
# Look before you leap

# print(name)
# number = int(input("Enter a number: "))

try:
    print(name)
except NameError:
    print("Sorry, the variable name does not have a value yet.")

try:
    number = input("Enter a number: ")
    number = int(number)  # can cause a ValueError if the user enters a letter
    print(number)
except ValueError:
    print("Invalid number")
except NameError:
    print("Sorry, the variable name does not have a value yet.")

print("The end of the process.")
