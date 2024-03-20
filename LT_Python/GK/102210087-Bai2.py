M = 0
N = 0
matrix = []
column_list = []
with open('E:/Viet/Python/LT_Python/GK/InpSortColumn.txt', 'r') as file:
    line = file.readlines()
    M,N = line[0].split()
    for i in range(1, len(line)): 
        row = list(map(int, line[i].split())) 
        matrix.append(row) 

for j in range(0, int(N)):
    column = [row[j] for row in matrix]
    sorted_column = sorted(column)
    column_list.append(sorted_column)

with open('E:/Viet/Python/LT_Python/GK/OutSortColumn.txt', 'w') as file:
    for k in range(0, int(M)):
        line = ' '.join(str(column[k]) for column in column_list)
        file.write(line + "\n")
