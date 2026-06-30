import sqlite3
from langchain_core.tools import tool


# Create a Custom Tool
@tool
def get_player_stats(player_name: str):
    """
    Returns the statistics of a cricket player from the database.
    """

    # Connect to the database
    conn = sqlite3.connect("players.db")
    cursor = conn.cursor()

    # Search for the player
    cursor.execute(
        "SELECT * FROM players WHERE player_name = ?",
        (player_name,)
    )

    # Get the result
    result = cursor.fetchone()

    # Close the connection
    conn.close()

    # Return the result
    if result:
        return result

    return "Player not found."


# -------------------------
# Test the Tool
# -------------------------

player = input("Enter Player Name: ")

# Manually invoke the tool
response = get_player_stats.invoke(
    {"player_name": player}
)

print("\nResult:")
print(response)

# Display Tool Metadata
print("\nTool Name:")
print(get_player_stats.name)

print("\nTool Description:")
print(get_player_stats.description)

print("\nTool Arguments:")
print(get_player_stats.args)