import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6]])
print(f"{A} - {A.dtype}")
B = np.array([[1.2, 2.3, 3.4], [4.5, 5.6, 6.7]])
print(f"{B} - {B.dtype}")
C = B.astype('i')
print(f"{C} - {C.dtype}")