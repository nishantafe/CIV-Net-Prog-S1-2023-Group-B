number = input("Enter a number: ")
valid_number = False
while not valid_number:
    try:
        number = int(number)
        print(number, "is a valid number, thank you!")
        valid_number = True
    except ValueError:
        number = input("Invalid number. Enter a valid number: ")

