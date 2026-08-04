# Program: display the Lucas sequence up to Ln

# Ask for the value of n
n = int(input("Enter the value of n: "))

# Check if n is valid
if n < 0:
    print("\nError: n must be a non-negative integer (n >= 0).")
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