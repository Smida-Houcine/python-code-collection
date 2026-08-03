# Program: calculate the least common multiple (LCM) of two non-negative integers a and b

# Ask for the values of a and b
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

# Check that a and b are valid
if a < 0 or b < 0:
    print("\nError: a and b must be non-negative integers (a >= 0 and b >= 0).")
# Special case: a = 0 or b = 0
elif a == 0 or b == 0:
    print(f"\nThe LCM of {a} and {b} is: 0")
else:
    # Calculate the GCD using the Euclidean algorithm
    x = a
    y = b
    while y != 0:
        remainder = x % y
        x = y
        y = remainder
    gcd = x
    # Calculate the LCM
    lcm = (a * b) // gcd
    # Display the result
    print(f"\nThe LCM of {a} and {b} is: {lcm}")
    
"""
    Calculate the GCD using the Euclidean algorithm
- Read the two numbers a and b.
- Divide the larger number by the smaller number and calculate the remainder.
- Replace the larger number with the smaller number, and replace the smaller number with the obtained remainder.
- Repeat the division and replacement steps while the remainder is not equal to 0.
- When the remainder becomes 0, the last non-zero remainder is the GCD of the two numbers.
- Display the GCD.
"""