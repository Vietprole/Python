import numpy as np

# Read the matrix from the input file
with open('E:\Viet\Python\LT_Python\DB\Mat.inp', "r") as file:
    lines = file.readlines()
    matrix = []
    for line in lines:
        row = [complex(num) for num in line.split()]
        matrix.append(row)

# Convert the matrix to a numpy array
matrix = np.array(matrix)
print(matrix)

# Check if the matrix is invertible
if np.linalg.det(matrix) == 0:
    # Calculate the pseudo-inverse of the matrix
    pseudo_inverse = np.linalg.pinv(matrix)
    result = pseudo_inverse.tolist()
    print("The matrix is not invertible. The pseudo-inverse is:")
else:
    # Calculate the inverse of the matrix
    inverse = np.linalg.inv(matrix)
    result = inverse.tolist()
    print("The matrix is invertible. The inverse is:")

print(result)
# Write the result to the output file
with open('E:\Viet\Python\LT_Python\DB\Mat.out', "w") as file:
    for row in result:
        file.write(" ".join([str(num) for num in row]) + "\n")