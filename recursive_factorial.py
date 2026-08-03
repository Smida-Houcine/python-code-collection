# Program: calculate factorial of a number n using a recursive method

# Define recursive factorial function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Ask for the value of n
n = int(input("Enter the value of n: "))

# Check that n is valid
if n < 0:
    print("\nError: n must be a non-negative integer (n >= 0).")
else:
    # Calculate and display factorial
    result = factorial(n)
    print(f"\n{n}! = {result}")