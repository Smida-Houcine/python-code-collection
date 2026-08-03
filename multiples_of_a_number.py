# Program: display multiples of a number

# Ask for the value of n
n = int(input("Enter the value of n: "))
# Ask for the number of multiples
m = int(input("Enter the number of multiples m: "))

# Check that m is valid
if m <= 0:
    print("\nError: the number of multiples m must be greater than 0 (m > 0).")
else:
    # Special case: n = 0
    if n == 0:
        print("\nThe multiples of 0 are:")
        print(0)
    else:
        print(f"\nThe first {m} multiples of {n} (starting from {n}, not including 0) are:")
        # Display multiples
        for i in range(1, m + 1):
            print(n * i, end=" ")
        print()