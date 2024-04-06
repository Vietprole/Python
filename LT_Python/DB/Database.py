import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('LT_Python/DB/qa.db')

# Create a cursor object
cursor = conn.cursor()

# Execute a query to fetch all data from a table
cursor.execute('select count(distinct answer) from qa')

# Fetch the first 10 rows from the result set
rows = cursor.fetchmany(10)

# Create a dataframe from the fetched rows
df = pd.DataFrame(rows)

# Print the dataframe
print(df)

# Close the cursor and the connection
cursor.close()
conn.close()