cars = ["Mercedes", "Volvo", "Ferrari", "Mazda"]
cars.append("Toyota")  # use .append() to add an item to a list
print("Cars", cars)

# Regular for loop with appending
favourite_cars = []
for item in cars:
    if "r" in item:
        favourite_cars.append(item)
print("My favourite cars are:", favourite_cars)

# List comprehension
best_cars = [item for item in cars if "r" in item]
print("Best cars:", best_cars)

grades = [22, 44, 66, 34, 12, 99]
# Condition to succeed, student's grade should be 50 or greater
successful_students_grades = ["Grade: " + str(grade) for grade in grades if (grade >= 50)]
successful_students_grades1 = ["Passed with: " + str(grade) if grade >= 50 else "Failed" for grade in grades]
results = ["Passed" if grade >= 50 else "Failed" for grade in grades]

failed_students_grades = ["Grade: " + str(grade) for grade in grades if grade < 50]
print("Successful students grades:", successful_students_grades)
print("Successful students grades1:", successful_students_grades1)
print("Failed students grades:", failed_students_grades)
print("Results", results)

