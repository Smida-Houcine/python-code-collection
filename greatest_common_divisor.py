# Program: calculate the greatest common divisor (GCD) of two non-negative integers a and b

# Ask for the values of a and b
a_value = input("Enter the value of a (a >= 0): ")
b_value = input("Enter the value of b (b >= 0): ")

# Check if inputs are empty
if len(a_value.strip()) == 0 or len(b_value.strip()) == 0:
    print("\nError: a and b must be entered.")
    exit()
try:
    # Convert inputs to integers
    a = int(a_value)
    b = int(b_value)
except ValueError:
    # Display an error message if inputs are not integers
    print("\nError: a and b must be integers.")
    exit()

# Check that a and b are valid
if a < 0 or b < 0:
    print("\nError: a and b must be non-negative (a >= 0 and b >= 0).")
# Special case: a = 0 and b = 0
elif a == 0 and b == 0:
    print(f"\nThe greatest common divisor (GCD) of {a} and {b} is undefined.")
else:
    # Copy a and b into temporary variables
    x = a
    y = b
    # Calculate the GCD using the Euclidean algorithm
    while y != 0:
        remainder = x % y
        x = y
        y = remainder
    # Display the result
    print(f"\nThe greatest common divisor (GCD) of {a} and {b} is: {x}")
    
"""
    Calculate the GCD using the Euclidean algorithm
- Read the two numbers a and b.
- Divide the larger number by the smaller number and calculate the remainder.
- Replace the larger number with the smaller number, and replace the smaller number with the obtained remainder.
- Repeat the division and replacement steps while the remainder is not equal to 0.
- When the remainder becomes 0, the last non-zero remainder is the GCD of the two numbers.
- Display the GCD.
"""
