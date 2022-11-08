import numpy as np
import matplotlib.pyplot as plt

A = 12
f = 50
num_terms = 100


def c(k: int):
    if k % 2 == 1:
        return 0
    return (2 * A / np.pi) / (1 - k * k)


def tk(k: int, t: float):
    return c(k) * np.exp(1j * 2 * np.pi * k * f * t)


def x(t: float):
    ans = 0
    for k in range(-num_terms // 2, num_terms // 2):
        ans += tk(k, t)
    return ans


def main():
    N = 400  # number of samples
    t = np.linspace(0, 3 / f, N)
    x_t = np.vectorize(x)(t)

    plt.plot(t, A * np.abs(np.sin(2 * np.pi * f * t)))
    plt.plot(t, np.abs(x_t), '.')

    plt.grid()
    plt.xlabel('t')
    plt.ylabel('x(t)')
    plt.legend([r'$A_0 \sin(2\pi f_0 t)$', 'Summation'])

    plt.plot()
    plt.savefig("../figs/Ex2_3_verify_xt.pdf")
    plt.show()


if __name__ == '__main__':
    main()
