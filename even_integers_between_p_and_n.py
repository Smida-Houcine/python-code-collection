# Program: calculate operations on even integers between p and n

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
    # Create a list of even integers
    even_integers = []
    for i in range(p, n + 1):
        if i % 2 == 0:
            even_integers.append(i)
    # Count even integers
    even_count = len(even_integers)
    # Display the number of even integers
    print(f"\nNumber of even integers between {p} and {n}: {even_count}")
    # Check if there are even integers
    if even_count == 0:
        print("There are no even integers.")
    else:
        # Display even integers
        print("Even integers:")
        for i in even_integers:
            print(i, end=" ")
        print()
        # Calculate the sum of even integers
        sum_even = 0
        for i in even_integers:
            sum_even = sum_even + i
        # Calculate the product of even integers
        product_even = 1
        for i in even_integers:
            product_even = product_even * i
        # Calculate the sum of powers of even integers
        sum_powers_even = 0
        for i in even_integers:
            sum_powers_even = sum_powers_even + i ** m
        # Calculate the product of powers of even integers
        product_powers_even = 1
        for i in even_integers:
            product_powers_even = product_powers_even * (i ** m)
        # Display results
        print(f"\nSum of even integers: {sum_even}")
        print(f"Product of even integers: {product_even}")
        print(f"Sum of powers of even integers with exponent {m}: {sum_powers_even}")
        print(f"Product of powers of even integers with exponent {m}: {product_powers_even}")
else:
    # Error message
    print("\nError: p must be non-negative (p >= 0), n must be greater than or equal to p (n >= p), and m must satisfy m >= 1.")
