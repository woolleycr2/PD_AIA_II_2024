import numpy as np

A = np.loadtxt("date.csv", delimiter=",")
print(np.amin(A, 0), np.amax(A, 0))
print(np.amin(A, 1), np.amax(A, 1), np.sum(A, 1))