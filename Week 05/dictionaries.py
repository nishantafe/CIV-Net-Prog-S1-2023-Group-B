my_dictionary = {"firstname": "John", "lastname": "Smith", "postcode": "2000"}

# Get the keys of a dictionary
keys = my_dictionary.keys()
print("Keys:", keys)

# Get the values of a dictionary
values = my_dictionary.values()
print("Values:", values)

# Get the items (pairs) of a dictionary
items = my_dictionary.items()
print("Items:", items)

# Get the value of a specific key in the dictionary
the_one = my_dictionary["firstname"]
print(the_one)

# Add a new item (pair) to the dictionary
my_dictionary["phone"] = "0412345678"
print(my_dictionary)

# Use a for loop with .items() to neatly display keys and values if a dictionary
for one_key, one_value in my_dictionary.items():
    print(one_key, one_value)

print(my_dictionary["postcode"])
