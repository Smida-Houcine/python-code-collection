# Program: calculate operations on even integers between p and n

# Ask for the starting integer
p = int(input("Enter the starting integer p: "))
# Ask for the ending integer
n = int(input("Enter the ending integer n: "))
# Ask for the exponent
m = int(input("Enter the exponent m (1 <= m <= 4): "))

# Check that the interval and exponent are valid
if p <= n and 1 <= m <= 4:
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
    print("\nError: p must be less than or equal to n and m must be between 1 and 4.")