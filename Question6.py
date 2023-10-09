import psycopg2
from collections import Counter

# Define the list of colors
colors = [
    "ARSH", "BROWN", "GREEN", "BROWN", "BLUE", "BLUE",
    "BLEW", "PINK", "PINK", "ORANGE", "ORANGE", "RED",
    "WHITE", "BLUE", "WHITE", "WHITE", "BLUE", "BLUE", "BLUE",
]

# Count the occurrences of each color
color_counts = Counter(colors)

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    database="your_database_name",
    user="your_username",
    password="your_password",
    host="your_host",
    port="your_port"
)

# Create a cursor object
cursor = conn.cursor()

# Create a table to store colors and their frequencies
cursor.execute("CREATE TABLE IF NOT EXISTS color_frequencies (color VARCHAR(255), frequency INT)")

# Insert color frequencies into the table
for color, frequency in color_counts.items():
    cursor.execute("INSERT INTO color_frequencies (color, frequency) VALUES (%s, %s)", (color, frequency))

# Commit the changes
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

print("Color frequencies have been saved to the database.")
