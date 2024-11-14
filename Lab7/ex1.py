import numpy as np
import matplotlib.pyplot as plt

tf = 2
fs = 500
q = 0.5

t = np.arange(0, tf, 1/fs)
x = 6 + 5 * (np.sin(2 * np.pi ** 2 * t) / (2 * np.pi ** 2 * t))
xc = np.round(x / q) * q