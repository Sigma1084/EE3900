import numpy as np
import matplotlib.pyplot as plt

A = 12
f = 50


def c(k: int):
    if k % 2 == 1:
        return 0
    return (2 * A / np.pi) / (1 - k*k)


def main():
    N = 1000
    t = np.linspace(0, 3 / f, N)
    B = np.ones(N) + 1j * np.zeros(N)

    plt.plot(t, np.abs(A * np.sin(2 * np.pi * f * t)))
    plt.plot(t, np.abs(np.fft.ifft(B)))

    plt.grid()
    plt.xlabel('t')
    plt.ylabel('x(t)')
    plt.plot()
    plt.savefig("../figs/Ex1_1_xt.pdf")
    plt.show()


if __name__ == '__main__':
    main()