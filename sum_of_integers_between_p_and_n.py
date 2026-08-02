# Program: calculate the sum of integers between p and n

# Ask for the starting integer
p = int(input("Enter the starting integer p: "))
# Ask for the ending integer
n = int(input("Enter the ending integer n: "))

# Check that the interval is valid
if p <= n:
    # Case where there is only one integer
    if p == n:
        print(f"\nThe only integer between {p} and {n} is {p}.")
        print(f"The sum is: {p}")
    else:
        # Initialize the sum
        total = 0
        # Calculate the sum of integers between p and n
        for i in range(p, n + 1):
            total = total + i
        # Display the result
        print(f"\nThe sum of integers from {p} to {n} is: {total}")
else:
    # Error message if p is greater than n
    print("\nError: p must be less than or equal to n.")