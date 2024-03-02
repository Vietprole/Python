import pandas as pd

# Read the CSV file
df = pd.read_csv('Meta.csv', index_col=0)
# Divide each cell in the "Win" column by the total in the "Win" column
# and store the results in a new column "Win rate"
df['Win rate'] = df['Win'].div(df['Pick'])

# Write the DataFrame back to the CSV file
df.to_csv('Meta.csv')