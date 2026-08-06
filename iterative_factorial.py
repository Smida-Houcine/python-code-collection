# Program: calculate factorial of a number n using an iterative method

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
    # Calculate factorial iteratively
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i
    # Display result
    print(f"\n{n}! = {factorial}")
else:
    # Error message
    print("\nError: n must be non-negative (n >= 0).")
