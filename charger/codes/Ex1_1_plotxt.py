import numpy as np
from matplotlib import pyplot as plt


def main():
    A = 12
    f = 50
    t = np.linspace(0, 3 / f, 1000)
    plt.plot(t, np.abs(A * np.sin(2 * np.pi * f * t)))
    plt.grid()
    plt.xlabel('t')
    plt.ylabel('x(t)')
    plt.plot()
    plt.savefig("../figs/Ex1_1_xt.pdf")
    plt.show()


if __name__ == '__main__':
    main()
