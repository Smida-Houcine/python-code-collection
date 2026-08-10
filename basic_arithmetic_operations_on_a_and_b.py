# Program: perform basic arithmetic operations on a and b

# Ask for the first number
a_value = input("Enter the first number: ")
# Ask for the second number
b_value = input("Enter the second number: ")

# Check if inputs are empty
if len(a_value.strip()) == 0 or len(b_value.strip()) == 0:
    print("\nError: both numbers must be entered.")
    exit()
try:
    # Convert inputs to floating-point numbers
    a = float(a_value)
    b = float(b_value)
except ValueError:
    # Display an error message if inputs are not numbers
    print("\nError: both inputs must be numbers.")
    exit()

# Calculate the addition
addition = a + b

# Calculate the multiplication
multiplication = a * b

# Calculate the subtraction of b from a
subtraction_a_minus_b = a - b

# Calculate the subtraction of a from b
subtraction_b_minus_a = b - a

# Display the results
print(f"\n1. Addition: {addition}")
print(f"2. Multiplication: {multiplication}")
print(f"3. Subtraction of b from a (a - b): {subtraction_a_minus_b}")
print(f"4. Subtraction of a from b (b - a): {subtraction_b_minus_a}")

# Calculate the division of a by b
if b != 0:
    division_a_by_b = a / b
    # Display the results
    print(f"5. Division of a by b (a / b): {division_a_by_b}")
else:
    # Display an error message if b is zero
    print("5. Division of a by b (a / b): undefined (division by zero is not allowed).")

# Calculate the division of b by a
if a != 0:
    division_b_by_a = b / a
    # Display the results
    print(f"6. Division of b by a (b / a): {division_b_by_a}")
else:
    # Display an error message if a is zero
    print("6. Division of b by a (b / a): undefined (division by zero is not allowed).")