import numpy as np

A = np.array([[1, 0, 1], [0, 1, 0], [1, 1, 1]], dtype=np.dtype(float))
b = np.array([10, 4, 8], dtype=np.dtype(float))

d = np.linalg.det(A)
x = np.linalg.solve(A, b)

print(d)