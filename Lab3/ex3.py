import numpy as np

A = np.array([[2, -3], [3, -2]])
B = np.array([[8], [-5]])
print(np.linalg.solve(A, B))