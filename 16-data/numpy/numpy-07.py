import numpy as np

# Create two matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix multiplication
C = np.matmul(A, B)
print("Matrix Multiplication:")
print(C)

# Matrix determinant
det_A = np.linalg.det(A)
print("Determinant of A:", det_A)

# Matrix inverse
inv_A = np.linalg.inv(A)
print("Inverse of A:")
print(inv_A)

# Eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues:")
print(eigenvalues)
print("Eigenvectors:")
print(eigenvectors)


