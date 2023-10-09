# Define the list of colors in RGB format
colors_rgb = [
    (0, 128, 0),    # GREEN
    (139, 69, 19),  # BROWN
    (0, 128, 0),    # GREEN
    (0, 0, 255),    # BLUE
    (0, 0, 255),    # BLUE
    (0, 0, 255),    # BLUE
    # ... (other colors)
]

# Function to convert RGB to grayscale intensity
def rgb_to_grayscale(rgb):
    r, g, b = rgb
    return 0.299 * r + 0.587 * g + 0.114 * b

# Convert colors to grayscale intensities
grayscale_intensities = [rgb_to_grayscale(color) for color in colors_rgb]

# Calculate the mean of grayscale intensities
mean_intensity = sum(grayscale_intensities) / len(grayscale_intensities)

# Calculate the variance
variance = sum((x - mean_intensity) ** 2 for x in grayscale_intensities) / len(grayscale_intensities)

print(f"The variance of the grayscale intensities of colors is: {variance:.2f}")
