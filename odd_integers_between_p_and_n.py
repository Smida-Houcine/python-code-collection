# Program: calculate operations on odd integers between p and n

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
    # Create a list of odd integers
    odd_integers = []
    for i in range(p, n + 1):
        if i % 2 != 0:
            odd_integers.append(i)
    # Count odd integers
    odd_count = len(odd_integers)
    # Display the number of odd integers
    print(f"\nNumber of odd integers between {p} and {n}: {odd_count}")
    # Check if there are odd integers
    if odd_count == 0:
        print("There are no odd integers.")
    else:
        # Display odd integers
        print("Odd integers:")
        for i in odd_integers:
            print(i, end=" ")
        print()
        # Calculate the sum of odd integers
        sum_odd = 0
        for i in odd_integers:
            sum_odd = sum_odd + i
        # Calculate the product of odd integers
        product_odd = 1
        for i in odd_integers:
            product_odd = product_odd * i
        # Calculate the sum of powers of odd integers
        sum_powers_odd = 0
        for i in odd_integers:
            sum_powers_odd = sum_powers_odd + i ** m
        # Calculate the product of powers of odd integers
        product_powers_odd = 1
        for i in odd_integers:
            product_powers_odd = product_powers_odd * (i ** m)
        # Display results
        print(f"\nSum of odd integers: {sum_odd}")
        print(f"Product of odd integers: {product_odd}")
        print(f"Sum of powers of odd integers with exponent {m}: {sum_powers_odd}")
        print(f"Product of powers of odd integers with exponent {m}: {product_powers_odd}")
else:
    # Error message
    print("\nError: p must be non-negative (p >= 0), n must be greater than or equal to p (n >= p), and m must satisfy m >= 1.")
