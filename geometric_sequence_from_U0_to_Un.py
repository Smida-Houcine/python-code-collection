"""
Written by: SMIDA Houcine L. 2026

Program: calculate terms and sum of a geometric sequence from U0 to Un
with common ratio q, where n >= 0

A geometric sequence is a sequence where
the quotient between two consecutive terms is constant.

The quotient between two consecutive terms is:
U(n + 1) / Un = q, if Un != 0

Therefore:
(U(n + 1) / Un) is constant whenever Un != 0.

The recurrence relation is:
U(n + 1) = q * Un

The first term of the sequence is U0.

The terms look like:
U0, U0 * q, U0 * q^2, U0 * q^3, ...

The term of index n is:
Un = U0 * q^n

The sequence calculated by this program is:
U0, U1, U2, ..., Un

The number of terms from U0 to Un is:
n + 1

The sum of the (n + 1) terms from U0 to Un is:
Sn = U0 + U1 + U2 + ... + Un

If q != 1:
Sn = U0 * (1 - q^(n + 1)) / (1 - q)
Equivalently:
Sn = U0 * (q^(n + 1) - 1) / (q - 1)
Sn = (q * Un - U0) / (q - 1)

If q = 1:
Sn = (n + 1) * U0
"""

# Display the purpose of the program
print("Calculate a geometric sequence from U0 to Un with common ratio q")
print()

# Enter the first term U0
U0_value = input("Enter the first term U0: ")
# Enter the common ratio q
q_value = input("Enter the common ratio, q: ")
# Enter the index of the last term n
n_value = input("Enter the index of the last term, n (n >= 0): ")

# Check if inputs are empty
if (
    len(U0_value.strip()) == 0
    or len(q_value.strip()) == 0
    or len(n_value.strip()) == 0
):
    print("\nError: all values must be entered.")
    exit()
# Alternative shorter version:
# if any(len(value.strip()) == 0 for value in (U0_value, q_value, n_value)):
try:
    # Convert U0 and q to floating-point numbers
    U0 = float(U0_value)
    q = float(q_value)
    # Convert n to an integer
    n = int(n_value)
except ValueError:
    # Display an error message if inputs are not valid numbers
    print("\nError: U0 and q must be numbers, and n must be an integer.")
    exit()

# Check if n is non-negative
if n < 0:
    print("\nError: n must be a non-negative integer (n >= 0).")
    exit()

# Generate the terms from U0 to Un
# Handle q = 0 separately to avoid 0^0.
if q == 0:
    terms = [U0] + [0.0] * n
else:
    terms = [U0 * q ** i for i in range(n + 1)]

# Calculate the term of index n
Un = U0 if q == 0 and n == 0 else U0 * q ** n

# Calculate the number of terms
number_of_terms = n + 1

# Calculate the sum of the terms from U0 to Un
if q != 1:
    Sn = U0 * (1 - q ** number_of_terms) / (1 - q)
else:
    Sn = number_of_terms * U0

# Check the type of the geometric sequence
if n > 0:
    # Case 1: U0 = 0
    if U0 == 0:
        print("\nThe sequence is constant at zero.")
    # Case 2: U0 > 0
    elif U0 > 0:
        if q > 1:
            print("\nThe sequence is increasing.")
        elif q == 1:
            print("\nThe sequence is constant.")
        elif q == 0:
            print("\nThe sequence becomes zero after U0.")
        elif 0 < q < 1:
            print("\nThe sequence is decreasing.")
        elif q == -1:
            print("\nThe sequence alternates between two values (U0 and -U0).")
        elif q < -1:
            print("\nThe sequence alternates with increasing absolute value.")
        elif -1 < q < 0:
            print("\nThe sequence alternates with decreasing absolute value.")
    # Case 3: U0 < 0
    elif U0 < 0:
        if q > 1:
            print("\nThe sequence is decreasing.")
        elif q == 1:
            print("\nThe sequence is constant.")
        elif 0 < q < 1:
            print("\nThe sequence is increasing.")
        elif q == 0:
            print("\nThe sequence becomes zero after U0.")
        elif q == -1:
            print("\nThe sequence alternates between two values (U0 and -U0).")
        elif q < -1:
            print("\nThe sequence alternates with increasing absolute value.")
        elif -1 < q < 0:
            print("\nThe sequence alternates with decreasing absolute value.")

# Display the terms from U0 to Un
print(f"\nTerms from U0 to U{n}: {terms}")

# Display the parameters
print(f"\nFirst term: U0 = {U0}")
print(f"Common ratio: q = {q}")
print(f"Index of the last term: n = {n}")

# Display the last term
print(f"Last term: U{n} = {Un}")
# Display the number of terms
print(f"Number of terms: {number_of_terms}")
# Display the sum of the terms from U0 to Un
print(f"Sum from U0 to U{n}: S{n} = {Sn}")