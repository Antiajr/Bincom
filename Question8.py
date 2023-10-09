import Question8

# Generate a random 4-digit binary number
binary_number = ''.join([random.choice('01') for _ in range(4)])

# Convert the binary number to base-10 (decimal)
decimal_number = int(binary_number, 2)

# Print the generated binary and decimal numbers
print(f"Generated Binary Number: {binary_number}")
print(f"Converted Decimal Number: {decimal_number}")
