import numpy as np

C = np.array([[2, -4, 1], [6, 3, 2], [3, -2, 4]])
print(C.shape)
print(C.T)
print(np.linalg.det(C))
print(np.linalg.inv(C))
print(np.linalg.matrix_rank(C))
