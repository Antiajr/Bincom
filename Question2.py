# Define the list of colors and their corresponding numerical representations (RGB)
colors = [
    ("ARSH", (0, 0, 0)),      # ARSH
    ("BROWN", (139, 69, 19)), # BROWN
    ("GREEN", (0, 128, 0)),   # GREEN
    ("BROWN", (139, 69, 19)), # BROWN
    ("BLUE", (0, 0, 255)),    # BLUE
    ("BLUE", (0, 0, 255)),    # BLUE
    ("BLEW", (0, 0, 255)),    # BLEW (Assuming this is a typo for "BLUE")
    ("PINK", (255, 192, 203)),# PINK
    ("PINK", (255, 192, 203)),# PINK
    ("ORANGE", (255, 165, 0)),# ORANGE
    ("ORANGE", (255, 165, 0)),# ORANGE
    ("RED", (255, 0, 0)),      # RED
    ("WHITE", (255, 255, 255)),# WHITE
    ("BLUE", (0, 0, 255)),    # BLUE
    ("WHITE", (255, 255, 255)),# WHITE
    ("WHITE", (255, 255, 255)),# WHITE
    ("BLUE", (0, 0, 255)),    # BLUE
    ("BLUE", (0, 0, 255)),    # BLUE
    ("BLUE", (0, 0, 255)),    # BLUE
]

# Sort the colors based on their numerical representations (RGB)
sorted_colors = sorted(colors, key=lambda x: x[1])

# Find the color in the middle (median)
median_color = sorted_colors[len(sorted_colors) // 2][0]

print(f"The median color is {median_color}.")
