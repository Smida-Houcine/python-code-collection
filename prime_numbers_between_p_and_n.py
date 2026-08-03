# Program: calculate operations on prime numbers between p and n

# Ask for the starting integer
p = int(input("Enter the starting integer p: "))
# Ask for the ending integer
n = int(input("Enter the ending integer n: "))
# Ask for the exponent
m = int(input("Enter the exponent m (1 <= m <= 4): "))

# Function to check if a number is prime
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
# Check that the interval and exponent are valid
if p <= n and 1 <= m <= 4:
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
    print("\nError: p must be less than or equal to n and m must be between 1 and 4.")