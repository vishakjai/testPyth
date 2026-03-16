import numpy as np

def calculate_determinant(matrix):
    """Calculate the determinant of a given matrix using NumPy."""
    return np.linalg.det(matrix)

# Example usage
if __name__ == "__main__":
    matrix = np.array([[1, 2], [3, 4]])
    determinant = calculate_determinant(matrix)
    print(f"Determinant: {determinant}")
