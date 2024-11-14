import numpy as np
import matplotlib.pyplot as plt

tf = 0.1
f = 25
fs_1 = 1000
fs_2 = 40
defazaj = np.pi / 6
A = 1
t_1 = np.arange(0, tf + 1 / fs_1, 1 / fs_1)
t_2 = np.arange(0, tf + 1 / fs_2, 1 / fs_2)
x_1 = A * np.sin(2 * np.pi * f * t_1 + defazaj)
x_2 = A * np.sin(2 * np.pi * f * t_2 + defazaj)

plt.plot(t_1, x_1, t_2, x_2)
plt.show()

