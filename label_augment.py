with open('E:/Viet/Python/LT_Python/GK/InpSortColumn.txt', 'r') as file:
    lines = file.readlines()
    data = []
    for line in lines:
        columns = line.split()
        # Switch columns 4 and 5 (0-indexed)
        columns[3], columns[4] = columns[4], columns[3]
        # Switch columns 2 and 3 (0-indexed)
        columns[1], columns[2] = columns[2], columns[1]
        data.append(columns)

# Write the modified data to another text file
with open('E:/Viet/Python/LT_Python/GK/OutSortColumn.txt', 'w') as file:
    for row in data:
        file.write(' '.join(row) + '\n')