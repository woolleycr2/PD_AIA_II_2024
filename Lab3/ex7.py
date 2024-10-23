import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[8, 10], [8, 5], [1, 5]])

A_1 = A + 5
print(A_1)
A_2 = A - 5
print(A_2)
A_3 = A * 5
print(A_3)
A_4 = A / 5
print(A_4)

print(A + B.T)
print(A - B.T)
print(A * B.T)
print(A / B.T)

print(A @ B)
print((A @ B) @ np.linalg.inv(A @ B))
