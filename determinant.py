import numpy as np

def calculate_determinant(matrix):
    return np.linalg.det(matrix)

# Example usage
matrix = np.array([[1, 2], [3, 4]])
det = calculate_determinant(matrix)
print(f"Determinant: {det}")
