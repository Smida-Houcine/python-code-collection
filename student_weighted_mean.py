# Calculate the weighted mean of a student's grades

# Get the number of courses
while True:
    n_input = input("Number of courses: ")
    if n_input.isdigit() and int(n_input) > 0:
        n = int(n_input)
        break
    print("Invalid input. Enter a positive integer.")

# Initialize totals
total = 0.0
total_coefficients = 0.0

# List of allowed coefficients
valid_coefficients = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]

# Enter grades and coefficients for each course
for i in range(1, n + 1):
    # Get and validate the grade
    while True:
        try:
            note = float(input(f"Course {i} note: "))
            # Grade must be between 0 and 20
            # and must be a multiple of 0.25
            if 0 <= note <= 20 and (note * 4).is_integer():
                break
            print("Invalid note.")
            print("Enter a value between 0 and 20")
            print("using increments of 0.25.")
            print("Examples: 12, 12.25, 12.5, 12.75")
        except ValueError:
            print("Invalid input. Please enter a number.")
    # Get and validate the coefficient
    while True:
        try:
            coefficient = float(input(f"Course {i} coefficient: "))
            if coefficient in valid_coefficients:
                break
            print("Invalid coefficient.")
            print("Choose from:", valid_coefficients)
        except ValueError:
            print("Invalid input. Please enter a number.")
    # Add the weighted grade
    total = total + note * coefficient
    total_coefficients = total_coefficients + coefficient

# Calculate the weighted mean
mean = total / total_coefficients

# Display the result
print()
print(f"Mean = {mean:.2f}")

# Determine the result and mention
if mean < 10:
    print("Result: Repeat")
elif mean < 12:
    print("Result: Pass (Fair)")
elif mean < 14:
    print("Result: Pass (Fairly Good)")
elif mean < 16:
    print("Result: Pass (Good)")
elif mean < 18:
    print("Result: Pass (Very Good)")
else:
    print("Result: Pass (Excellent)")