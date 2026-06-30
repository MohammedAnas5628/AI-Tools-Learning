import sqlite3

# Connect to the database
conn = sqlite3.connect("players.db")

# Create a cursor
cursor = conn.cursor()

# Get player name from the user
player = input("Enter Player Name: ")

# Execute SQL query
cursor.execute(
    "SELECT * FROM players WHERE player_name = ?",
    (player,)
)

# Fetch one record
result = cursor.fetchone()

# Display the result
print(result)

# Close the connection
conn.close()