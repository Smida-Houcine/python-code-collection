# Written by: SMIDA Houcine L. 2026
# Program: solve an equation of the form ax^2 + bx + c = 0

# Display the purpose of the program
print("Solve an equation of the form ax^2 + bx + c = 0")
print()

# Enter the coefficient a
a_value = input("Enter the coefficient a: ")
# Enter the coefficient b
b_value = input("Enter the coefficient b: ")
# Enter the coefficient c
c_value = input("Enter the coefficient c: ")

# Check if inputs are empty
if len(a_value.strip()) == 0 or len(b_value.strip()) == 0 or len(c_value.strip()) == 0:
    print("\nError: all coefficients must be entered.")
    exit()
try:
    # Convert inputs to floating-point numbers
    a = float(a_value)
    b = float(b_value)
    c = float(c_value)
except ValueError:
    # Display an error message if inputs are not numbers
    print("\nError: a, b, and c must be numbers.")
    exit()

# Case 1: a, b, and c are all non-zero
if a != 0 and b != 0 and c != 0:
    # Display the equation with its coefficients
    print(f"\nThe equation is: ({a})x^2 + ({b})x + ({c}) = 0")
    # Calculate the discriminant
    delta = b ** 2 - 4 * a * c
    # Display the discriminant
    print(f"\nDiscriminant (Delta) = {delta}")
    # Check the number of real solutions
    if delta > 0:
        # Calculate the two real solutions
        x1 = (-b - delta ** 0.5) / (2 * a)
        x2 = (-b + delta ** 0.5) / (2 * a)
        print("The equation has two distinct real solutions.")
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")
    elif delta == 0:
        # Calculate the double real solution
        x = -b / (2 * a)
        print("The equation has one double real solution.")
        print(f"x1 = x2 = {x}")
    else:
        # Display a message when there is no real solution
        print("The equation has no real solution.")

# Case 2: a and b are non-zero, but c is zero
elif a != 0 and b != 0 and c == 0:
    # Display the equation with its coefficients
    print(f"\nThe equation is: ({a})x^2 + ({b})x = 0")
    # Calculate the two real solutions
    x1 = 0
    x2 = -b / a
    print("The equation has two distinct real solutions.")
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")

# Case 3: a is non-zero, b is zero, and c is non-zero
elif a != 0 and b == 0 and c != 0:
    # Display the equation with its coefficients
    print(f"\nThe equation is: ({a})x^2 + ({c}) = 0")
    # Calculate -c / a
    value = -c / a
    # Check the sign of -c / a (a and c are non-zero)
    # Since a and c are non-zero, value is also non-zero
    if value > 0:
        # Calculate the two real solutions
        x1 = value ** 0.5
        x2 = -value ** 0.5
        print("The equation has two distinct real solutions.")
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")
    else:
        # Display a message when there is no real solution
        print("The equation has no real solution.")

# Case 4: a is non-zero, b and c are both zero
elif a != 0 and b == 0 and c == 0:
    # Display the equation with its coefficients
    print(f"\nThe equation is: ({a})x^2 = 0")
    # Calculate the double real solution
    x = 0
    print("The equation has one double real solution.")
    print(f"x1 = x2 = {x}")

# Case 5: a is zero, but b and c are non-zero 
elif a == 0 and b != 0 and c != 0:
    # Display the equation with its coefficients
    print(f"\nThe equation is linear: ({b})x + ({c}) = 0")
    # Calculate the real solution
    x = -c / b
    print("The equation has one real solution.")
    print(f"x = {x}")

# Case 6: a is zero, b is non-zero, and c is zero
elif a == 0 and b != 0 and c == 0:
    # Display the equation with its coefficients
    print(f"\nThe equation is linear: ({b})x = 0")
    # Calculate the real solution
    x = 0
    print("The equation has one real solution.")
    print(f"x = {x}")

# Case 7: a and b are zero, but c is non-zero
elif a == 0 and b == 0 and c != 0:
    # Display the equation with its coefficients
    print(f"\nThe equation is: ({c}) = 0")
    print("The equation has no real solution.")

# Case 8: a, b, and c are all zero
else:
    # Display the equation with its coefficients
    print("\nThe equation is: 0 = 0")
    print("The equation has infinitely many real solutions.")

# Cases 5 and 6 could be combined into a single case:
# a is zero and b is non-zero.
# They are kept separate here for educational purposes.