import random

for attempt in range(10):
    random_number = random.randint(1, 100)
    print(f"Attempt {attempt + 1}: ", end="")
    if random_number >= 50:
        print("Heads")
    else:
        print("Tails")

