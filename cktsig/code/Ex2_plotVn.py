import numpy as np
from matplotlib import pyplot as plt

def vt(t: float):
    if t <= 0:
        return 0
    return (4/3) * (1 - np.exp(-1.5 * 10**6 * t))

def main():
    num_vt = np.vectorize(vt, otypes=['double'])
    t = np.linspace(0, 1e-5, 10000)
    V = num_vt(t)
    plt.plot(t, V)
    plt.xlabel('t (s)')
    plt.ylabel('$v_{c_0}(t)$ (V)')
    plt.grid()
    plt.plot()
    plt.savefig('../figs/Ex2_vn.pdf')
    # plt.show()

if __name__ == '__main__':
    main()

