import numpy as np
import matplotlib.pyplot as plt

A = 12
f = 50
num_terms = 100


def c(k: int):
    if k % 2 == 1:
        return 0
    return (2 * A / np.pi) / (1 - k * k)


def a(k: int):
    if k == 0:
        return c(0)
    else:
        return c(k) + c(-k)


def b(k: int):
    return c(k) - c(-k)


def tk(k: int, t: float):
    return a(k) * np.cos(2 * np.pi * k * f * t) + \
           b(k) * np.sin(2 * np.pi * k * f * t)


def x(t: float):
    ans = 0
    for k in range(num_terms // 2):
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
    plt.savefig("../figs/Ex2_4_verify_xt_real.pdf")
    plt.show()


if __name__ == '__main__':
    main()
