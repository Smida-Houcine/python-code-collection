"""
Written by: SMIDA Houcine L. 2026

Program: calculate terms and sum of a geometric sequence from Up to Un
with common ratio q, where p >= 0 and n >= p

A geometric sequence is a sequence where
the quotient between two consecutive terms is constant.

The quotient between two consecutive terms is:
U(n + 1) / Un = q, if Un != 0

Therefore:
(U(n + 1) / Un) is constant whenever Un != 0.

The recurrence relation is:
U(n + 1) = q * Un

The first term of the sequence is Up.

The terms look like:
Up, Up * q, Up * q^2, Up * q^3, ...

The term of index n is:
Un = Up * q^(n - p)

The sequence calculated by this program is:
Up, U(p + 1), U(p + 2), ..., Un

The number of terms from Up to Un is:
n - p + 1

The sum of the (n - p + 1) terms from Up to Un is:
S_p_n = Up + U(p + 1) + ... + Un

If q != 1:
S_p_n = Up * (1 - q^(n - p + 1)) / (1 - q)
Equivalently:
S_p_n = Up * (q^(n - p + 1) - 1) / (q - 1)
S_p_n = (q * Un - Up) / (q - 1)

If q = 1:
S_p_n = (n - p + 1) * Up
"""

# Display the purpose of the program
print("Calculate a geometric sequence from Up to Un with common ratio q")
print()

# Enter the first term Up
Up_value = input("Enter the first term Up: ")
# Enter the index p
p_value = input("Enter the index of the first term, p (p >= 0): ")
# Enter the common ratio q
q_value = input("Enter the common ratio, q: ")
# Enter the index of the last term n
n_value = input("Enter the index of the last term, n (n >= p): ")

# Check if inputs are empty
if (
    len(Up_value.strip()) == 0
    or len(p_value.strip()) == 0
    or len(q_value.strip()) == 0
    or len(n_value.strip()) == 0
):
    print("\nError: all values must be entered.")
    exit()
# Alternative shorter version:
# if any(len(value.strip()) == 0 for value in (Up_value, p_value, q_value, n_value)):
try:
    # Convert Up and q to floating-point numbers
    Up = float(Up_value)
    q = float(q_value)
    # Convert p and n to integers
    p = int(p_value)
    n = int(n_value)
except ValueError:
    # Display an error message if inputs are not valid numbers
    print("\nError: Up and q must be numbers, and p and n must be integers.")
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
# Handle q = 0 separately to avoid 0^0.
if q == 0:
    terms = [Up] + [0.0] * (n - p)
else:
    terms = [Up * q ** (i - p) for i in range(p, n + 1)]

# Calculate the term of index n
Un = Up * q ** (n - p) if not (q == 0 and n == p) else Up

# Calculate the number of terms
number_of_terms = n - p + 1

# Calculate the sum of the terms from Up to Un
if q != 1:
    S_p_n = Up * (1 - q ** number_of_terms) / (1 - q)
else:
    S_p_n = number_of_terms * Up

# Check the type of the geometric sequence
if n > p:
    # Case 1: Up = 0
    if Up == 0:
        print("\nThe sequence is constant at zero.")
    # Case 2: Up > 0
    elif Up > 0:
        if q > 1:
            print("\nThe sequence is increasing.")
        elif q == 1:
            print("\nThe sequence is constant.")
        elif q == 0:
            print(f"\nThe sequence becomes zero after U{p}.")
        elif 0 < q < 1:
            print("\nThe sequence is decreasing.")
        elif q == -1:
            print(f"\nThe sequence alternates between two values (U{p} and -U{p}).")
        elif q < -1:
            print("\nThe sequence alternates with increasing absolute value.")
        elif -1 < q < 0:
            print("\nThe sequence alternates with decreasing absolute value.")
    # Case 3: Up < 0
    elif Up < 0:
        if q > 1:
            print("\nThe sequence is decreasing.")
        elif q == 1:
            print("\nThe sequence is constant.")
        elif 0 < q < 1:
            print("\nThe sequence is increasing.")
        elif q == 0:
            print(f"\nThe sequence becomes zero after U{p}.")
        elif q == -1:
            print(f"\nThe sequence alternates between two values (U{p} and -U{p}).")
        elif q < -1:
            print("\nThe sequence alternates with increasing absolute value.")
        elif -1 < q < 0:
            print("\nThe sequence alternates with decreasing absolute value.")

# Display the terms from Up to Un
print(f"\nTerms from U{p} to U{n}: {terms}")

# Display the parameters
print(f"\nFirst term: U{p} = {Up}")
print(f"Index of the first term: p = {p}")
print(f"Common ratio: q = {q}")
print(f"Index of the last term: n = {n}")

# Display the last term
print(f"Last term: U{n} = {Un}")
# Display the number of terms
print(f"Number of terms: {number_of_terms}")
# Display the sum of the terms from Up to Un
print(f"Sum from U{p} to U{n}: S_{p}_{n} = {S_p_n}")