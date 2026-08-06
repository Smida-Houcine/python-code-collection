# Program: display multiples of a number

# Ask for the value of n
n_value = input("Enter the value of n (n >= 0): ")
# Ask for the number of multiples
m_value = input("Enter the number of multiples m (m > 0): ")

# Check if inputs are empty
if len(n_value.strip()) == 0 or len(m_value.strip()) == 0:
    print("\nError: n and m must be entered.")
    exit()
try:
    # Convert inputs to integers
    n = int(n_value)
    m = int(m_value)
except ValueError:
    # Display an error message if inputs are not integers
    print("\nError: n and m must be integers.")
    exit()

# Check that the values are valid
if n >= 0 and m > 0:
    # Special case: n = 0
    if n == 0:
        print(f"\nThe only multiple of {n} is:")
        print(n)
    else:
        print(f"\nThe first {m} multiples of {n} (starting from {n}, not including 0) are:")
        # Display multiples
        for i in range(1, m + 1):
            print(n * i, end=" ")
        print()
else:
    # Error message
    print("\nError: n must be non-negative (n >= 0), and the number of multiples m must satisfy m > 0.")
