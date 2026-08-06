# Program: find and display positive divisors of a number n

# Ask for the value of n
n_value = input("Enter the value of n (n >= 0): ")

# Check if input is empty
if len(n_value.strip()) == 0:
    print("\nError: n must be entered.")
    exit()
try:
    # Convert input to integer
    n = int(n_value)
except ValueError:
    # Display an error message if the input is not an integer
    print("\nError: n must be an integer.")
    exit()

# Check that n is valid
if n < 0:
    print("\nError: n must be non-negative (n >= 0).")
# Special case: n = 0
elif n == 0:
    print(f"\nEvery positive integer is a divisor of {n}.")
elif n == 1:
    print(f"\nThe only positive divisor of {n} is {n}.")
else:
    # Find the positive divisors of n
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    # Display the divisors
    print(f"\nThe {len(divisors)} positive divisors of {n} are:")
    for divisor in divisors:
        print(divisor, end=" ")
    print()
