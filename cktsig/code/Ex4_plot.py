import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import os

yt = sp.vectorize(lambda t: 0 if t < 0 else 2 / 3 * (1 - np.exp(-1.5e6 * t)))
yn = sp.vectorize(lambda n: 0 if n < 0 else 2 / 3 * (1 - (1-7.5e5*1e-7) ** (n*1e7) / (1 + 7.5e5 * 1e-7) ** (n * 1e7)))
spice = np.loadtxt('Ex4_output.dat')

T = np.linspace(0, 5e-6, 100)

plt.plot(T, yt(T), label='$y(t)$ using Inverse Laplace')
plt.plot(spice[:, 0], spice[:, 1], 'o', label='ngspice')
plt.plot(T, yn(T), '.', label='$y(n)$ using Inverse Z-Transform')
plt.grid()
plt.legend()
plt.savefig('../figs/Ex4.pdf')
# plt.show()
os.system("sh gopen.sh ..figs/Ex4.pdf")
