"""
Written by: SMIDA Houcine L. 2026
Program: calculate terms and sum of an arithmetic sequence from U0 to Un with common difference r

An arithmetic sequence is a sequence where
the difference between any two consecutive terms is constant.

The first term of the sequence is U0.

The terms look like:
U0, U0 + r, U0 + 2 * r, U0 + 3 * r, ...

The recurrence relation is:
U(n + 1) = Un + r

The nth term is:
Un = U0 + n * r

The sequence calculated by this program is:
U0, U1, U2, ..., Un

The sum of the first (n + 1) terms is:
Sn = U0 + U1 + U2 + ... + Un

Sn = ((n + 1) / 2) * (U0 + Un)
Sn = ((n + 1) / 2) * (2 * U0 + n * r)
"""

# Display the purpose of the program
print("Calculate an arithmetic sequence from U0 to Un with common difference r")
print()

# Enter the first term U0
U0_value = input("Enter the first term U0: ")
# Enter the common difference r
r_value = input("Enter the common difference r: ")
# Enter the index of the last term n
n_value = input("Enter the index of the last term n: ")

# Check if inputs are empty
if len(U0_value.strip()) == 0 or len(r_value.strip()) == 0 or len(n_value.strip()) == 0:
    print("\nError: all values must be entered.")
    exit()
try:
    # Convert U0 and r to floating-point numbers
    U0 = float(U0_value)
    r = float(r_value)
    # Convert n to an integer
    n = int(n_value)
except ValueError:
    # Display an error message if inputs are not valid numbers
    print("\nError: U0 and r must be numbers, and n must be an integer.")
    exit()

# Check if n is non-negative
if n < 0:
    print("\nError: n must be a non-negative integer (n >= 0).")
    exit()

# Check the type of the arithmetic sequence
if r > 0:
    print("\nThe sequence is increasing.")
elif r < 0:
    print("\nThe sequence is decreasing.")
else:
    print("\nThe sequence is constant.")

# Display the parameters
print(f"\nFirst term: U0 = {U0}")
print(f"Common difference: r = {r}")
print(f"Index of the last term: n = {n}")
# Display the number of terms from U0 to Un
print(f"Number of terms: {n + 1}")

# Generate the terms from U0 to Un
terms = [U0 + i * r for i in range(n + 1)]

# Calculate the nth term
Un = U0 + n * r

# Calculate the sum of the terms from U0 to Un
Sn = ((n + 1) / 2) * (2 * U0 + n * r)

# Display the terms from U0 to Un
print(f"\nTerms from U0 to U{n}: {terms}")
# Display the nth term
print(f"U{n} = {Un}")
# Display the sum of the first n + 1 terms
print(f"S{n} = {Sn}")