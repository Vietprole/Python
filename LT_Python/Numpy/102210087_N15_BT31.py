import numpy as np

class MatCalc:
    def __init__(self, matrix):
        self.matrix = matrix

    def norm(self):
        return np.linalg.norm(self.matrix)

    def trace(self):
        return np.trace(self.matrix)

    def determinant(self):
        return np.linalg.det(self.matrix)

    def inverse(self):
        if self.matrix.shape[0] != self.matrix.shape[1]:
            raise ValueError("Matrix must be square to find its inverse.")
        return np.linalg.inv(self.matrix)

# example
A = np.array([[1, 2], [3, 4]])
calc = MatCalc(A)
print(calc.norm())
print(calc.trace())
print(calc.determinant())
print(calc.inverse())