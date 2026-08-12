"""
Written by: SMIDA Houcine L. 2026

Program: calculate terms and sum of an arithmetic sequence from Up to Un
with common difference r, where p >= 0 and n >= p

An arithmetic sequence is a sequence where
the difference between any two consecutive terms is constant.

The first term of the sequence is Up.

The terms look like:
Up, Up + r, Up + 2 * r, Up + 3 * r, ...

The recurrence relation is:
U(n + 1) = Un + r

The term of index n is:
Un = Up + (n - p) * r

The sequence calculated by this program is:
Up, U(p + 1), U(p + 2), ..., Un

The number of terms from Up to Un is:
n - p + 1

The sum of the (n - p + 1) terms from Up to Un is:
S_p_n = Up + U(p + 1) + ... + Un

S_p_n = ((n - p + 1) / 2) * (Up + Un)
S_p_n = ((n - p + 1) / 2) * (2 * Up + (n - p) * r)
"""

# Display the purpose of the program
print("Calculate an arithmetic sequence from Up to Un with common difference r")
print()

# Enter the first term Up
Up_value = input("Enter the first term Up: ")
# Enter the index p
p_value = input("Enter the index of the first term, p (p >= 0): ")
# Enter the common difference r
r_value = input("Enter the common difference, r: ")
# Enter the index of the last term n
n_value = input("Enter the index of the last term, n (n >= p): ")

# Check if inputs are empty
if (
    len(Up_value.strip()) == 0
    or len(p_value.strip()) == 0
    or len(r_value.strip()) == 0
    or len(n_value.strip()) == 0
):
    print("\nError: all values must be entered.")
    exit()
# Alternative shorter version:
# if any(len(value.strip()) == 0 for value in (Up_value, p_value, r_value, n_value)):
try:
    # Convert Up and r to floating-point numbers
    Up = float(Up_value)
    r = float(r_value)
    # Convert p and n to integers
    p = int(p_value)
    n = int(n_value)
except ValueError:
    # Display an error message if inputs are not valid numbers
    print("\nError: Up and r must be numbers, and p and n must be integers.")
    exit()

# Check if p is non-negative
if p < 0:
    print("\nError: p must be a non-negative integer (p >= 0).")
    exit()

# Check if n is greater than or equal to p
if n < p:
    print("\nError: n must be greater than or equal to p (n >= p).")
    exit()

# Generate the terms from Up to Un
terms = [Up + (i - p) * r for i in range(p, n + 1)]

# Calculate the term of index n
Un = Up + (n - p) * r

# Calculate the sum of the terms from Up to Un
S_p_n = ((n - p + 1) / 2) * (2 * Up + (n - p) * r)

# Check the type of the arithmetic sequence
if n > p:
    if r > 0:
        print("\nThe sequence is increasing.")
    elif r < 0:
        print("\nThe sequence is decreasing.")
    else:
        print("\nThe sequence is constant.")

# Display the terms from Up to Un
print(f"\nTerms from U{p} to U{n}: {terms}")

# Display the parameters
print(f"\nFirst term: U{p} = {Up}")
print(f"Index of the first term: p = {p}")
print(f"Common difference: r = {r}")
print(f"Index of the last term: n = {n}")

# Display the last term
print(f"Last term: U{n} = {Un}")
# Number of terms from Up to Un
print(f"Number of terms: {n - p + 1}")
# Display the sum of the (n - p + 1) terms from Up to Un
print(f"Sum from U{p} to U{n}: S_{p}_{n} = {S_p_n}")
