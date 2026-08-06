# Program: display the Lucas sequence up to Ln

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

# Check if n is valid
if n < 0:
    print("\nError: n must be non-negative (n >= 0).")
else:
    print(f"\nLucas sequence from L0 to L{n}:")
    # First Lucas numbers
    l0 = 2
    l1 = 1
    # Display L0
    print(l0, end=" ")
    if n >= 1:
        # Display L1
        print(l1, end=" ")
        # Display L2 to Ln
        for i in range(2, n + 1):
            ln = l0 + l1
            print(ln, end=" ")
            # Update Lucas numbers
            l0 = l1
            l1 = ln
    print()

"""
Lucas sequence:
L0 = 2
L1 = 1
Ln = L(n-1) + L(n-2), for n >= 2
"""
