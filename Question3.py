from collections import Counter

# Define the list of colors
colors = [
    "ARSH",
    "BROWN",
    "GREEN",
    "BROWN",
    "BLUE",
    "BLUE",
    "BLEW",
    "PINK",
    "PINK",
    "ORANGE",
    "ORANGE",
    "RED",
    "WHITE",
    "BLUE",
    "WHITE",
    "WHITE",
    "BLUE",
    "BLUE",
    "BLUE",
]

# Count the occurrences of each color
color_counts = Counter(colors)

# Find the color with the maximum count
most_worn_color, count = color_counts.most_common(1)[0]

print(f"The color mostly worn throughout the week is {most_worn_color}.")
