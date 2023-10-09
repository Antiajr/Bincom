from PIL import Image
import numpy as np

# Define the list of colors in RGB format
colors = [
    (0, 128, 0),    # GREEN
    (255, 255, 0),  # YELLOW
    (0, 128, 0),    # GREEN
    (139, 69, 19),  # BROWN
    (0, 0, 255),    # BLUE
    (255, 192, 203),# PINK
    (0, 0, 255),    # BLUE
    (255, 255, 0),  # YELLOW
    (255, 165, 0),  # ORANGE
    (255, 255, 224),# CREAM
    (255, 165, 0),  # ORANGE
    (255, 0, 0),    # RED
    (255, 255, 255),# WHITE
    (0, 0, 255),    # BLUE
    (255, 255, 255),# WHITE
    (0, 0, 255),    # BLUE
    (0, 0, 255),    # BLUE
    (0, 0, 255),    # BLUE
    (0, 128, 0)     # GREEN
]

# Calculate the mean RGB value
mean_color = tuple(np.mean(colors, axis=0).astype(int))

# Create an image with the mean color
width, height = 100, 100  # You can specify the image dimensions
image = Image.new("RGB", (width, height), mean_color)

# Save or display the image
image.show()  # Display the image


