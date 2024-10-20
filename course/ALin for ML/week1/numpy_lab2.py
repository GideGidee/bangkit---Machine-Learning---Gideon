import numpy as np
import matplotlib.pyplot as plt
from utils import plot_lines

A = np.array([[-1, 3], [3, 2]], dtype=np.dtype(float))

b = np.array([7, 1], dtype=np.dtype(float))

print("Matrix A:")
print(A)
print("\nArray b:")
print(b)

x = np.linalg.solve(A, b)

print(f"Solution: {x}")


# ===============================================================

# determinant
d = np.linalg.det(A)

print(f"Determinant of matrix A: {d:.2f}")

# ====================================================

# visualizing
A_system = np.hstack((A, b.reshape((2, 1))))

plot_lines(A_system)

# =============================================================

# with no solution
A_2 = np.array([[-1, 3], [3, -9]], dtype=np.dtype(float))

b_2 = np.array([7, 1], dtype=np.dtype(float))

d_2 = np.linalg.det(A_2)

print(f"Determinant of matrix A_2: {d_2:.2f}")

A_2_system = np.hstack((A_2, b_2.reshape((2, 1))))
print(A_2_system)

plot_lines(A_2_system)

# ===========================================================

# with infinite number solution
b_3 = np.array([7, -21], dtype=np.dtype(float))
A_3_system = np.hstack((A_2, b_3.reshape((2, 1))))
print(A_3_system)
plot_lines(A_3_system)
