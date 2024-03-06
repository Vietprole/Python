import pandas as pd

# Read the CSV file
df = pd.read_csv('Meta-Viet.csv', index_col=0)

# Get 10 strings from the console in the same line, separated by spaces
pick_inputs = input("Enter 10 champs picked (5 Win, 5 Lose) separated by spaces: ").split()

# Check each string
for pick_input in pick_inputs[:5]:
    # Check if the string exists in the DataFrame index
    if pick_input in df.index:
        # Increment the "Pick" attribute
        df.loc[pick_input, 'Pick'] += 1
        # Increment the "Win" attribute
        df.loc[pick_input, 'Win'] += 1

# Loop through the rest of the pick_inputs
for pick_input in pick_inputs[5:]:
    # Check if the string exists in the DataFrame index
    if pick_input in df.index:
        # Increment the "Pick" attribute
        df.loc[pick_input, 'Pick'] += 1

# Get 8 strings from the console in the same line, separated by spaces
ban_inputs = input("Enter 8 champs banned separated by spaces: ").split()

# Check each string
for ban_input in ban_inputs:
    # Check if the string exists in the DataFrame index
    if ban_input in df.index:
        # Increment the "Pick" attribute
        df.loc[ban_input, 'Ban'] += 1

# Add a new row with index name "Total" to store the sum of each column
df.loc['Total'] = df.iloc[:-1].sum()

# Divide each cell in the "Pick" column by the total in the "Pick" column
# and store the results in a new column "Pick rate"
df['Pick rate'] = df['Pick'].div(df.loc['Total', 'Pick'])

# Divide each cell in the "Ban" column by the total in the "Ban" column
# and store the results in a new column "Ban rate"
df['Ban rate'] = df['Ban'].div(df.loc['Total', 'Ban'])

# Divide each cell in the "Win" column by the total in the "Win" column
# and store the results in a new column "Win rate"
df['Win rate'] = df['Win'].div(df['Pick'])

# Round the values in the "Ban rate", "Pick rate", and "Win rate" columns to two decimal places
# and convert them to percentages
df['Ban rate'] = df['Ban rate'].mul(100).round(2)
df['Pick rate'] = df['Pick rate'].mul(100).round(2)
df['Win rate'] = df['Win rate'].mul(100).round(2)

# Write the DataFrame back to the CSV file
df.to_csv('Meta-Viet.csv')