# Program: calculate the sum of integers between p and n

# Ask for the starting integer
p_value = input("Enter the starting integer p (p >= 0): ")
# Ask for the ending integer
n_value = input("Enter the ending integer n (n >= p): ")

# Check if inputs are empty
if len(p_value.strip()) == 0 or len(n_value.strip()) == 0:
    print("\nError: p and n must be entered.")
    exit()
try:
    # Convert inputs to integers
    p = int(p_value)
    n = int(n_value)
except ValueError:
    # Display an error message if inputs are not integers
    print("\nError: p and n must be integers.")
    exit()

# Check that the interval is valid
if p >= 0 and n >= p:
    # Case where there is only one integer
    if p == n:
        print(f"\nThe only integer between {p} and {n} is: {p}")
        print(f"The sum is: {p}")
    else:
        # Count the integers
        count = n - p + 1
        # Display the integers
        print(f"\nThe {count} integers from {p} to {n} are:")
        for i in range(p, n + 1):
            print(i, end=" ")
        print()
        # Initialize the sum
        total = 0
        # Calculate the sum of integers between p and n
        for i in range(p, n + 1):
            total = total + i
        # Display the result
        print(f"\nThe sum of integers from {p} to {n} is: {total}")
else:
    # Error message
    print("\nError: p must be non-negative (p >= 0) and n must be greater than or equal to p (n >= p).")
