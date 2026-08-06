# Program: calculate the product of powers m of integers between p and n

# Ask for the starting integer
p_value = input("Enter the starting integer p (p >= 0): ")
# Ask for the ending integer
n_value = input("Enter the ending integer n (n >= p): ")
# Ask for the exponent
m_value = input("Enter the exponent m (m >= 1): ")

# Check if inputs are empty
if len(p_value.strip()) == 0 or len(n_value.strip()) == 0 or len(m_value.strip()) == 0:
    print("\nError: p, n and m must be entered.")
    exit()
try:
    # Convert inputs to integers
    p = int(p_value)
    n = int(n_value)
    m = int(m_value)
except ValueError:
    # Display an error message if inputs are not integers
    print("\nError: p, n and m must be integers.")
    exit()

# Check that the interval and exponent are valid
if p >= 0 and n >= p and m >= 1:
    # Note about large powers
    print("\nNote: m should not be too large because powers grow very quickly.")
    # Case where there is only one integer
    if p == n:
        result = p ** m
        print(f"\nThe only integer between {p} and {n} is: {p}.")
        print(f"The product of powers with exponent {m} is: {result}")
    else:
        # Count the integers
        count = n - p + 1
        # Display the integers
        print(f"\nThe {count} integers from {p} to {n} are:")
        for i in range(p, n + 1):
            print(i, end=" ")
        print()
        # Initialize the product
        product = 1
        # Calculate the product of powers of integers between p and n
        for i in range(p, n + 1):
            product = product * (i ** m)
        # Display the result
        print(f"\nThe product of powers of integers from {p} to {n} with exponent {m} is: {product}")
else:
    # Error message
    print("\nError: p must be non-negative (p >= 0), n must be greater than or equal to p (n >= p), and m must satisfy m >= 1.")
