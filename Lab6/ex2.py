import numpy as np
import matplotlib.pyplot as plt

def interpolate_linear(t, x, tt):
            N = len(t)
            NN = len(tt)
            y = np.zeros((NN,))

            for k in range(0, NN):
                for i in range(0, N-1):
                    if(t[i] <= tt[k] and tt[k] <= t[i + 1]) or i == N - 2:
                        y[k] = x[i] + (x[i + 1] - x[i]) / (t[i + 1] - t[i]) * (tt[k] - t[i])
                        break
            return y
tf = 1
fs_1 = 5
fs_2 = 20
t_1 = np.arange(0, tf, 1 / fs_1)
t_2 = np.arange(0, tf, 1 / fs_2)
x_1 = np.sin(2 * np.pi * t_1)
x_2 = interpolate_linear(t_1, x_1, t_2)

plt.plot(t_2, x_2, 'o', t_1, x_1, "*")
plt.grid()
plt.legend(["fs_2", "fs_1"])
plt.show()


