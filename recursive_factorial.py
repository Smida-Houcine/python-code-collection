# Program: calculate factorial of a number n using a recursive method

# Define recursive factorial function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Ask for the value of n
n_value = input("Enter the value of n (n >= 0): ")

# Check if input is empty
if len(n_value.strip()) == 0:
    print("\nError: n must be entered.")
    exit()
try:
    # Convert input to integer
    n = int(n_value)
except ValueError:
    # Display an error message if the input is not an integer
    print("\nError: n must be an integer.")
    exit()

# Check that n is valid
if n >= 0:
    # Calculate and display factorial
    result = factorial(n)
    print(f"\n{n}! = {result}")
else:
    # Error message
    print("\nError: n must be non-negative (n >= 0).")
