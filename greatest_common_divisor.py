# Program: calculate the greatest common divisor (GCD) of two non-negative integers a and b

# Ask for the values of a and b
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

# Check that a and b are valid
if a < 0 or b < 0:
    print("\nError: a and b must be non-negative integers (a >= 0 and b >= 0).")
# Special case: a = 0 and b = 0
elif a == 0 and b == 0:
    print("\nThe GCD of 0 and 0 is undefined.")
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
    print(f"\nThe GCD of {a} and {b} is: {x}")