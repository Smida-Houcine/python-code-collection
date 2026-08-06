# Program: count and display even and odd integers between p and n

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
    # Initialize counters
    even_count = 0
    odd_count = 0
    # Count even and odd integers
    for i in range(p, n + 1):
        if i % 2 == 0:
            even_count = even_count + 1
        else:
            odd_count = odd_count + 1
    # Display the number of even integers
    print(f"\nNumber of even integers between {p} and {n}: {even_count}")
    # Display the even integers
    if even_count == 0:
        print("There are no even integers.")
    else:
        print("Even integers:")
        for i in range(p, n + 1):
            if i % 2 == 0:
                print(i, end=" ")
        print()
    # Display the number of odd integers
    print(f"\nNumber of odd integers between {p} and {n}: {odd_count}")
    # Display the odd integers
    if odd_count == 0:
        print("There are no odd integers.")
    else:
        print("Odd integers:")
        for i in range(p, n + 1):
            if i % 2 != 0:
                print(i, end=" ")
        print()
else:
    # Error message
    print("\nError: p must be non-negative (p >= 0) and n must be greater than or equal to p (n >= p).")
