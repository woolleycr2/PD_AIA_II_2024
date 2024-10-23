import numpy as np

D = np.array([[6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6], [-6, -5, -4, -3, -2, -1], [4, 5, 6, 7, 8, 9], [8, 7, 6, 5, 4, 3]])

print(D.shape)
print(type(D.shape))
i = int(D.shape[0])
j = int(D.shape[1])
print(i)
print(j)
E = D[3-1:, :3]
print(E)
F = D[:3, 3:]
print(F)
print(np.hstack((E, F)))
print(np.vstack((E, F)))
D_10x3 = np.reshape(D, (10, 3))
print(D_10x3)
np.savetxt("D_10x3.csv", D_10x3, delimiter=",")