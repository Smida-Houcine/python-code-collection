# Program: count and display even and odd integers between p and n

# Ask for the starting integer
p = int(input("Enter the starting integer p: "))
# Ask for the ending integer
n = int(input("Enter the ending integer n: "))

# Check that the interval is valid
if p <= n:
    # Initialize counters
    even_count = 0
    odd_count = 0
    # Count even and odd integers
    for i in range(p, n + 1):
        if i % 2 == 0:
            even_count = even_count + 1
        else:
            odd_count = odd_count + 1
    # Display the number of even integers
    print(f"\nNumber of even integers between {p} and {n}: {even_count}")
    # Display the even integers
    if even_count == 0:
        print("There are no even integers.")
    else:
        print("Even integers:")
        for i in range(p, n + 1):
            if i % 2 == 0:
                print(i, end=" ")
        print()
    # Display the number of odd integers
    print(f"\nNumber of odd integers between {p} and {n}: {odd_count}")
    # Display the odd integers
    if odd_count == 0:
        print("There are no odd integers.")
    else:
        print("Odd integers:")
        for i in range(p, n + 1):
            if i % 2 != 0:
                print(i, end=" ")
        print()
else:
    # Error message if p is greater than n
    print("\nError: p must be less than or equal to n.")