from matrix_utils import determinant


# 1x1
assert determinant([[5]]) == 5

# 2x2
assert determinant([[1, 2], [3, 4]]) == -2
assert determinant([[2, 4], [1, 2]]) == 0

# Identity
assert determinant([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 1

# 3x3 example (determinant = 1)
M = [[1, 2, 3], [0, 1, 4], [5, 6, 0]]
assert determinant(M) == 1

# Singular 3x3
assert determinant([[1, 2, 3], [2, 4, 6], [3, 6, 9]]) == 0

# Float matrix (determinant should be 0)
detf = determinant([[1.5, 2.0], [3.0, 4.0]])
assert abs(detf - 0.0) < 1e-9

print('OK')
