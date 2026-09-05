import pandas as pd
import sqlite3

# Read Excel file
df = pd.read_excel("questions.xlsx")

# Connect to SQLite database
conn = sqlite3.connect("questions.db")

# Store questions in database
df.to_sql(
    "questions",
    conn,
    if_exists="replace",
    index=False
)

# Close database connection
conn.close()

print("Questions imported successfully!")