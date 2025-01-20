from numpy import linalg
import numpy as np

def calculate_eigenvalues(matrix):
    n, m = np.array(matrix).shape
    if n != m:
        raise ValueError("Matrix A must be square (n x n).")
    eigenvalues = linalg.eigvals(matrix)
    return eigenvalues

print(calculate_eigenvalues(matrix = [[2, 1], [1, 2]]))