import numpy as np

# Input size of A, b
print("Matrix A(MxN): ")
M = int(input("Enter M: "))
N = int(input("Enter N: "))

# M >= N
while M < N:
    print("Error: M >= N.")
    print("Matrix A(MxN): ")
    M = int(input("Enter M: "))
    N = int(input("Enter N: "))

A = np.zeros((M, N))
b = np.zeros((M, 1))

# Input matrix A
print("Enter the elements of matrix A:")
for i in range(M):
    for j in range(N):
        A[i][j] = float(input(f"A[{i}][{j}]: "))

# Input vector b
print("Enter the elements of vector b:")
for i in range(M):
    b[i][0] = float(input(f"b[{i}]: "))

# Calculate the least squares solution
x = np.linalg.lstsq(A, b, rcond=None)[0]

print("The solution vector x is:")
print(x)