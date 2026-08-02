# Program: display integers between p and n

# Ask for the starting integer
p = int(input("Enter the starting integer p: "))
# Ask for the ending integer
n = int(input("Enter the ending integer n: "))

# Check that the interval is valid
if p <= n:
    # Case where there is only one integer
    if p == n:
        print(f"\nThe only integer between {p} and {n} is: {p}")
    else:
        # Calculate the number of integers in the interval
        number_of_integers = n - p + 1
        # Display the integers
        print(f"\nThe {number_of_integers} integers from {p} to {n} are:")
        for i in range(p, n + 1):
            print(i, end=" ")
        print()
else:
    # Error message if p is greater than n
    print("\nError: p must be less than or equal to n.")
