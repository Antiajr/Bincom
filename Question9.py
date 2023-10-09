def calculate_fibonacci(n):
    fib_sequence = [0, 1]

    while len(fib_sequence) < n:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)

    return fib_sequence

# Calculate the first 50 Fibonacci numbers
n = 50
fibonacci_sequence = calculate_fibonacci(n)

# Calculate the sum of the first 50 Fibonacci numbers
fibonacci_sum = sum(fibonacci_sequence)

# Print the sum
print(f"The sum of the first 50 Fibonacci numbers is: {fibonacci_sum}")
