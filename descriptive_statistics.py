# Program: calculate descriptive statistics of a list of numbers

# Ask the user to enter values separated by spaces
values = input("Enter the values separated by spaces: ")

# Check if at least one value was entered
if len(values.strip()) == 0:
    print("\nError: the list must contain at least one value.")
    exit()

try:
    # Split the input string into separate values
    # and convert each value into a float number
    numbers = [float(x) for x in values.split()]
    # Display the list of numbers
    print("\n", numbers)
except ValueError:
    # Display an error message if the user enters non-numeric values
    print("\nError: Please enter numbers only.")
    exit()

# Sort values
sorted_numbers = sorted(numbers)
# Display sorted values
print("\nSorted numbers:", "\n", sorted_numbers)

# Number of values
n = len(numbers)

# Minimum and maximum
minimum = min(numbers)
maximum = max(numbers)

# Range
data_range = maximum - minimum

# Sum
total = sum(numbers)

# Sum of squares
sum_of_squares = sum(x ** 2 for x in numbers)

# Arithmetic mean
mean = sum(numbers) / n

# Root mean square (RMS)
root_mean_square = (sum(x ** 2 for x in numbers) / n) ** 0.5

# Median
if n % 2 == 0:
    median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
else:
    median = sorted_numbers[n // 2]

# Mode
frequency = {}
for x in numbers:
    frequency[x] = frequency.get(x, 0) + 1

max_frequency = max(frequency.values())

if max_frequency == 1:
    mode = "No mode"
else:
    mode = [x for x in frequency if frequency[x] == max_frequency]
    if len(mode) == 1:
        mode = mode[0]

# Variance (population variance)
variance = (sum(x ** 2 for x in numbers) / n) - (sum(numbers) / n) ** 2
# variance = (sum((x - mean) ** 2 for x in numbers)) / n

# Standard deviation
standard_deviation = ((sum(x ** 2 for x in numbers) / n) - (sum(numbers) / n) ** 2) ** 0.5
# standard_deviation = variance ** 0.5

# Display results
print("\nDescriptive statistics:")

print(f"Number of values: {n}")
print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")
print(f"Range: {data_range}")
print(f"Sum: {total}")
print(f"Sum of squares: {sum_of_squares}")
print(f"Arithmetic mean: {mean}")
print(f"Root mean square (RMS): {root_mean_square}")
print(f"Median: {median}")
print(f"Mode: {mode}")
print(f"Variance: {variance}")
print(f"Standard deviation: {standard_deviation}")