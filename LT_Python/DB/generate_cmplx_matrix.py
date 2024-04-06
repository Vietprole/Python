import numpy as np

# Define the size of the matrix
rows = 5
cols = 5

# Generate a matrix of random complex numbers
# matrix = np.random.randint(rows, cols) + np.random.randint(rows, cols) * 1j

# Define the range of the random integers
low = 1
high = 10

# Generate a matrix of random integers
matrix = np.random.randint(low, high, (rows, cols)) + np.random.randint(low, high, (rows, cols)) * 1j

# Write the matrix to the input file
with open('E:\Viet\Python\LT_Python\DB\Mat.inp', 'w') as file:
    for row in matrix:
        for element in row:
            file.write(f'{element.real}+{element.imag}j ')
        file.write('\n')