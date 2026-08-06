# Program: display the Fibonacci sequence up to Fn

# Ask for the value of n
value = input("Enter the value of n: ")

# Check if the input is empty
if len(value.strip()) == 0:
    print("\nError: a value must be entered.")
    exit()
try:
    # Convert input to integer
    n = int(value)
except ValueError:
    # Display an error message if the input is not an integer
    print("\nError: n must be an integer.")
    exit()

# Check if n is valid
if n < 0:
    print("\nError: n must be a non-negative integer (n >= 0).")
    exit()
# Display Fibonacci sequence
print(f"\nFibonacci sequence from F0 to F{n}:")
# First Fibonacci numbers
f0 = 0
f1 = 1
# Display F0
print(f0, end=" ")
if n >= 1:
    # Display F1
    print(f1, end=" ")
    # Display F2 to Fn
    for _ in range(2, n + 1):
        fn = f0 + f1
        print(fn, end=" ")
        # Update Fibonacci numbers
        f0 = f1
        f1 = fn
print()

"""
Fibonacci sequence:
F0 = 0
F1 = 1
Fn = F(n-1) + F(n-2), for n >= 2
"""
