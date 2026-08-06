# Program: calculate operations on prime numbers between p and n

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

# Function to check if a number is prime
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
# Check that the interval and exponent are valid
if p >= 0 and n >= p and m >= 1:
    # Note about large powers
    print("\nNote: m should not be too large because powers grow very quickly.")
    # Create a list of prime numbers
    prime_numbers = []
    for i in range(p, n + 1):
        if is_prime(i):
            prime_numbers.append(i)
    # Count prime numbers
    prime_count = len(prime_numbers)
    # Display the number of prime numbers
    print(f"\nNumber of prime numbers between {p} and {n}: {prime_count}")
    # Check if there are prime numbers
    if prime_count == 0:
        print("There are no prime numbers.")
    else:
        # Display prime numbers
        print("Prime numbers:")
        for i in prime_numbers:
            print(i, end=" ")
        print()
        # Calculate the sum of prime numbers
        sum_prime = 0
        for i in prime_numbers:
            sum_prime = sum_prime + i
        # Calculate the product of prime numbers
        product_prime = 1
        for i in prime_numbers:
            product_prime = product_prime * i
        # Calculate the sum of powers of prime numbers
        sum_powers_prime = 0
        for i in prime_numbers:
            sum_powers_prime = sum_powers_prime + i ** m
        # Calculate the product of powers of prime numbers
        product_powers_prime = 1
        for i in prime_numbers:
            product_powers_prime = product_powers_prime * (i ** m)
        # Display results
        print(f"\nSum of prime numbers: {sum_prime}")
        print(f"Product of prime numbers: {product_prime}")
        print(f"Sum of powers of prime numbers with exponent {m}: {sum_powers_prime}")
        print(f"Product of powers of prime numbers with exponent {m}: {product_powers_prime}")
else:
    # Error message
    print("\nError: p must be non-negative (p >= 0), n must be greater than or equal to p (n >= p), and m must satisfy m >= 1.")
