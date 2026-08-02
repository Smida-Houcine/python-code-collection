# Program: calculate the product of powers m of integers between p and n

# Ask for the starting integer
p = int(input("Enter the starting integer p: "))
# Ask for the ending integer
n = int(input("Enter the ending integer n: "))
# Ask for the power (1 <= m <= 4)
m = int(input("Enter the power m (1 <= m <= 4): "))

# Check that the interval and the power are valid
if p <= n and 1 <= m <= 4:
    # Case where there is only one integer
    if p == n:
        result = p ** m
        print(f"\nThe only integer between {p} and {n} is {p}.")
        print(f"The product of powers with exponent {m} is: {result}")
    else:
        # Initialize the product
        product = 1
        # Calculate the product of powers between p and n
        for i in range(p, n + 1):
            product = product * (i ** m)
        # Display the result
        print(f"\nThe product of powers from {p} to {n} with exponent {m} is: {product}")
else:
    # Error message if the interval or power is invalid
    print("\nError: p must be less than or equal to n and m must be between 1 and 4.")