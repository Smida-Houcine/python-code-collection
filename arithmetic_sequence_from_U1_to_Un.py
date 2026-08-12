"""
Written by: SMIDA Houcine L. 2026

Program: calculate terms and sum of an arithmetic sequence from U1 to Un
with common difference r, where n >= 1

An arithmetic sequence is a sequence where
the difference between any two consecutive terms is constant.

The first term of the sequence is U1.

The terms look like:
U1, U1 + r, U1 + 2 * r, U1 + 3 * r, ...

The recurrence relation is:
U(n + 1) = Un + r

The term of index n is:
Un = U1 + (n - 1) * r

The sequence calculated by this program is:
U1, U2, U3, ..., Un

The number of terms from U1 to Un is:
n

The sum of the n terms from U1 to Un is:
Sn = U1 + U2 + U3 + ... + Un

Sn = (n / 2) * (U1 + Un)
Sn = (n / 2) * (2 * U1 + (n - 1) * r)
"""

# Display the purpose of the program
print("Calculate an arithmetic sequence from U1 to Un with common difference r")
print()

# Enter the first term U1
U1_value = input("Enter the first term U1: ")
# Enter the common difference r
r_value = input("Enter the common difference, r: ")
# Enter the index of the last term n
n_value = input("Enter the index of the last term, n (n >= 1): ")

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
    print("\nError: n must be a positive integer (n >= 1).")
    exit()

# Generate the terms from U1 to Un
terms = [U1 + (i - 1) * r for i in range(1, n + 1)]

# Calculate the term of index n
Un = U1 + (n - 1) * r

# Calculate the sum of the terms from U1 to Un
Sn = (n / 2) * (2 * U1 + (n - 1) * r)

# Check the type of the arithmetic sequence
if n > 1:
    if r > 0:
        print("\nThe sequence is increasing.")
    elif r < 0:
        print("\nThe sequence is decreasing.")
    else:
        print("\nThe sequence is constant.")

# Display the terms from U1 to Un
print(f"\nTerms from U1 to U{n}: {terms}")

# Display the parameters
print(f"\nFirst term: U1 = {U1}")
print(f"Common difference: r = {r}")
print(f"Index of the last term: n = {n}")

# Display the last term
print(f"Last term: U{n} = {Un}")
# Number of terms from U1 to Un
print(f"Number of terms: {n}")
# Display the sum of the n terms from U1 to Un
print(f"Sum from U1 to U{n}: S{n} = {Sn}")
