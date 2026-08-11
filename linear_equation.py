# Written by: SMIDA Houcine L. 2026
# Program: solve an equation of the form ax + b = 0

# Display the purpose of the program
print("Solve an equation of the form ax + b = 0")
print()
# Enter the coefficient a
a_value = input("Enter the coefficient a: ")
# Enter the coefficient b
b_value = input("Enter the coefficient b: ")

# Check if inputs are empty
if len(a_value.strip()) == 0 or len(b_value.strip()) == 0:
    print("\nError: all coefficients must be entered.")
    exit()
try:
    # Convert inputs to floating-point numbers
    a = float(a_value)
    b = float(b_value)
except ValueError:
    # Display an error message if inputs are not numbers
    print("\nError: a and b must be numbers.")
    exit()

# Case 1: a and b are both non-zero
if a != 0 and b != 0:
    # Display the equation with its coefficients
    print(f"\nThe equation is: ({a})x + ({b}) = 0")
    # Calculate the real solution
    x = -b / a
    print("The equation has one real solution.")
    print(f"x = {x}")

# Case 2: a is non-zero and b is zero
elif a != 0 and b == 0:
    # Display the equation with its coefficient
    print(f"\nThe equation is: ({a})x = 0")
    # Calculate the real solution
    x = 0
    print("The equation has one real solution.")
    print(f"x = {x}")

# Case 3: a is zero and b is non-zero
elif a == 0 and b != 0:
    # Display the equation with its coefficient
    print(f"\nThe equation is: ({b}) = 0")
    print("The equation has no real solution.")

# Case 4: a and b are both zero
else:
    # Display the equation
    print("\nThe equation is: 0 = 0")
    print("The equation has infinitely many real solutions.")

# Cases 1 and 2 could be combined into a single case:
# a is non-zero.
# They are kept separate here for educational purposes.