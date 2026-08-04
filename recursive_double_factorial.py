# Program: calculate the double factorial of a number n using a recursive method

# Define recursive double factorial function
def double_factorial(n):
    # Special cases: 0!! = 1 and (-1)!! = 1
    if n == 0 or n == -1:
        return 1
    else:
        return n * double_factorial(n - 2)

# Ask for the value of n
n = int(input("Enter the value of n: "))

# Check that n is valid
if n < -1:
    print("\nError: n must be an integer greater than or equal to -1 (n >= -1).")
else:
    # Calculate and display double factorial
    result = double_factorial(n)
    if n == -1:
        print(f"\n({n})!! = {result}")
    else:
        print(f"\n{n}!! = {result}")

"""
Compute the double factorial n!!
If n is even:  n!! = n × (n-2) × (n-4) × ... × 2
If n is odd:  n!! = n × (n-2) × (n-4) × ... × 1
with (-1)!! = 1 and 0!! = 1
"""
"""
For more details, see:
Arfken, G. (1985). Mathematical methods for physicists (3rd ed.). Academic Press.
Arfken, G. B., & Weber, H. J. (2005). Mathematical methods for physicists (6th ed.). Elsevier Academic Press.
"""