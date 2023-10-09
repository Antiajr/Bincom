# Define the list of colors
colors = [
    "ARSH", "BROWN", "GREEN", "BROWN", "BLUE", "BLUE",
    "BLEW", "PINK", "PINK", "ORANGE", "ORANGE", "RED",
    "WHITE", "BLUE", "WHITE", "WHITE", "BLUE", "BLUE", "BLUE",
]

# Count the occurrences of the color "red"
red_count = colors.count("RED")

# Calculate the total number of colors
total_colors = len(colors)

# Calculate the probability of choosing "red" at random
probability_red = red_count / total_colors

print(f"The probability of choosing the color 'red' at random is: {probability_red:.2%}")
