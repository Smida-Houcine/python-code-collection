# Program: calculate the product of integers between p and n

# Ask for the starting integer
p = int(input("Enter the starting integer p: "))
# Ask for the ending integer
n = int(input("Enter the ending integer n: "))

# Check that the interval is valid
if p <= n:
    # Case where there is only one integer
    if p == n:
        print(f"\nThe only integer between {p} and {n} is {p}.")
        print(f"The product is: {p}")
    else:
        # Initialize the product
        product = 1
        # Calculate the product of integers between p and n
        for i in range(p, n + 1):
            product = product * i
        # Display the result
        print(f"\nThe product of integers from {p} to {n} is: {product}")
else:
    # Error message if p is greater than n
    print("\nError: p must be less than or equal to n.")