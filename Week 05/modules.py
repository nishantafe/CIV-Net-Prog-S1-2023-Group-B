import random
import string
import time

random_number = random.randint(1, 10)
print("Random number:", random_number)

letters = string.ascii_letters  # Alphabet letters (upper & lower case)
digits = string.digits  # All numbers 0-9
symbols = string.punctuation  # All special characters/symbols
print("Letters:", letters)
print("Digits:", digits)
print("Symbols:", symbols)

# With random.choice(data) you can get 1 choice from the data
random_letter = random.choice(letters)  # Pick a letter from letters
random_digits = random.choice(digits)  # Pick a digit from digits
random_symbols = random.choice(symbols)  # Pick a symbol from symbols

print("Random letter:", random_letter)
print("Random digits:", random_digits)
print("Random symbols:", random_symbols)

character_limit = 50
my_magical_word = ""
for character in range(character_limit):
    my_magical_word += random.choice(letters + digits + symbols)
print("My magical word:", my_magical_word)

print(f"A message will be displayed in 3 seconds...")
time.sleep(3)  # Delay by 3 seconds
print("The 3 seconds are over. Thank you!")

print("Processing...")
for i in range(10):
    time.sleep(1)
    print(f"\r{i * 10 + 10}%", end="")
print("\nComplete")
