"""
Written by: SMIDA Houcine L. 2026
Program: calculate terms and sum of an arithmetic sequence

An arithmetic sequence is a sequence where
the difference between any two consecutive terms is constant.

The terms look like:
U1, U1 + r, U1 + 2 * r, U1 + 3 * r, ...

The nth term is:
Un = U1 + (n - 1) * r

The sum of the first n terms is:
Sn = (n / 2) * (U1 + Un)
Sn = (n / 2) * (2 * U1 + (n - 1) * r)
"""

# Display the purpose of the program
print("Calculate terms and sum of an arithmetic sequence")
print()

# Enter the first term U1
U1_value = input("Enter the first term U1: ")
# Enter the common difference r
r_value = input("Enter the common difference r: ")
# Enter the number of terms n
n_value = input("Enter the number of terms n: ")

# Check if inputs are empty
if len(U1_value.strip()) == 0 or len(r_value.strip()) == 0 or len(n_value.strip()) == 0:
    print("\nError: all values must be entered.")
    exit()
try:
    # Convert U1 and r to floating-point numbers
    U1 = float(U1_value)
    r = float(r_value)
    # Convert n to an integer
    n = int(n_value)
except ValueError:
    # Display an error message if inputs are not valid numbers
    print("\nError: U1 and r must be numbers, and n must be an integer.")
    exit()

# Check if n is positive
if n <= 0:
    print("\nError: n must be a positive integer (n > 0).")
    exit()

# Check the type of the arithmetic sequence
if r > 0:
    print("\nThe sequence is increasing.")
elif r < 0:
    print("\nThe sequence is decreasing.")
else:
    print("\nThe sequence is constant.")

# Display the parameters
print(f"\nFirst term: U1 = {U1}")
print(f"Common difference: r = {r}")
print(f"Number of terms: n = {n}")

# Generate the first n terms
terms = [U1 + (i - 1) * r for i in range(1, n + 1)]

# Calculate the nth term
Un = U1 + (n - 1) * r

# Calculate the sum of the first n terms
Sn = (n / 2) * (2 * U1 + (n - 1) * r)

# Display the terms
print(f"\nTerms of the sequence: {terms}")
# Display the nth term
print(f"U{n} = {Un}")
# Display the sum of the first n terms
print(f"S{n} = {Sn}")
