# Program: calculate operations on odd integers between p and n

# Ask for the starting integer
p = int(input("Enter the starting integer p: "))
# Ask for the ending integer
n = int(input("Enter the ending integer n: "))
# Ask for the exponent
m = int(input("Enter the exponent m (1 <= m <= 4): "))

# Check that the interval and exponent are valid
if p <= n and 1 <= m <= 4:
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
    print("\nError: p must be less than or equal to n and m must be between 1 and 4.")