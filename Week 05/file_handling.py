# Creating and opening a file for the purpose of re-writing
file_out = open("file.txt", "w")
file_out.write("This is the first line.\n")
file_out.write("This is the second line.\n")
file_out.close()

# Create and open a file for the purpose of appending (adding to existing content)
file_out_a = open("file_append.txt", "a")
file_out_a.write("This is a newly added (appended) line.\n")
file_out_a.close()

# Open an existing file for the purpose of reading
file_in = open("file.txt", "r")
print(file_in.read())
file_in.close()

phonebook_dictionary = {}
phonebook_file_in = open("phonebook.txt", "r")

for line in phonebook_file_in:
    # store name and phone after extracting them by splitting a line using the space seperator
    name, phone = line.split(" ")

    # add and associate a name with a phone number in the dictionary
    # use the .rstrip() to clean up the new line after each phone number
    phonebook_dictionary[name] = phone.rstrip()

phonebook_file_in.close()
print(phonebook_dictionary)

# Get a phone number by providing a name
print("Sara's phone number is", phonebook_dictionary["Sara"])

for name, phone in phonebook_dictionary.items():
    # print("Name:", name, "Phone:", phone)
    print(f"Name: {name:10s} Phone: {phone}")
