# Program: calculate factorial of a number n using an iterative method

# Ask for the value of n
n = int(input("Enter the value of n: "))

# Check that n is valid
if n < 0:
    print("\nError: n must be a non-negative integer (n >= 0).")
else:
    # Calculate factorial iteratively
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i
    # Display result
    print(f"\n{n}! = {factorial}")