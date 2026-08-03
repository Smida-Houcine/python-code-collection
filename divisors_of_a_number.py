# Program: find and display positive divisors of a number n

# Ask for the value of n
n = int(input("Enter the value of n: "))

# Check that n is valid
if n < 0:
    print("\nError: n must be a non-negative integer (n >= 0).")
# Special case: n = 0
elif n == 0:
    print("\nEvery non-zero positive integer is a divisor of 0.")
else:
    # Find the positive divisors of n
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    # Display the divisors
    print(f"\nThe {len(divisors)} divisors of {n} are:")
    for divisor in divisors:
        print(divisor, end=" ")
    print()