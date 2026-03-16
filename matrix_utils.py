"""Matrix utilities.

Provides `determinant(matrix)` which computes the determinant
of a square matrix (list of lists) using Gaussian elimination
with partial pivoting.
"""
from typing import List


def determinant(matrix: List[List[float]]) -> float:
    """Compute determinant of a square matrix.

    Args:
      matrix: square matrix as list of lists (rows).

    Returns:
      Determinant as float or int (converted to int if within 1e-9).

    Raises:
      ValueError: if matrix is not square.
    """
    # Validate
    n = len(matrix)
    if n == 0:
        return 1
    for row in matrix:
        if len(row) != n:
            raise ValueError("matrix must be square")

    # Make a copy as floats
    A = [list(map(float, row)) for row in matrix]
    sign = 1

    for i in range(n):
        # Partial pivoting: find row with max abs in column i
        pivot_row = max(range(i, n), key=lambda r: abs(A[r][i]))
        if abs(A[pivot_row][i]) < 1e-15:
            return 0
        if pivot_row != i:
            A[i], A[pivot_row] = A[pivot_row], A[i]
            sign *= -1

        pivot = A[i][i]
        # Eliminate below
        for j in range(i + 1, n):
            factor = A[j][i] / pivot
            # Update row j
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]

    det = sign
    for i in range(n):
        det *= A[i][i]

    # Return int when very close to integer
    if abs(det - round(det)) < 1e-9:
        return int(round(det))
    return det


__all__ = ["determinant"]
