import sqlite3
import pandas as pd

# Connect to SQLite database (creates players.db if it doesn't exist)
conn = sqlite3.connect("players.db")

# Read the CSV file
df = pd.read_csv("players.csv")

# Store the data into a table named 'players'
df.to_sql("players", conn, if_exists="replace", index=False)

# Close the database connection
conn.close()

print("Database created successfully!")