# input() is a function that gets an input from a user
# The data type will always be a string
# You can convert a string to an integer using int()

name = input("Enter your name: ")
score = int(input("Enter your current score: "))

print("Name:", name)
print("Score:", score)

print("Hey", name, "we'll give you a bonus of 10")
score += 10
print("Name:", name)
print("Score:", score)
