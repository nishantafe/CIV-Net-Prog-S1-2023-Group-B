"""You can use the split() method to extract data
based on a seperator (like space)"""

# num1 = 10
# num2 = 20
num1, num2 = 10, 20  # Same as the previous 2 lines
print(num1, num2)

record = "John 0423135431"
name, phone = record.split(" ")
print("Hi", name, "your phone number is", phone)
