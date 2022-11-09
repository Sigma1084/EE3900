import numpy as np
import matplotlib.pyplot as plt
import scipy


def main():
    vec_h = scipy.vectorize(lambda t: 100*np.sinc(100*t), otypes=['double'])
    vec_x = scipy.vectorize(lambda t: 12*np.abs(np.sin(2*np.pi*50*t)), otypes=['double'])
    t_step = 100000
    z = np.linspace(-1e5, 1e5, t_step)
    o = np.linspace(0, 2e5, t_step)
    y = np.convolve(vec_h(z), vec_x(z))
    plt.plot((5*np.pi/24)*y*2, label='simulation')
    p = 5*np.ones(100000)
    plt.plot(o, p, label="$5$V")
    plt.legend()
    plt.grid()
    plt.savefig("../figs/Ex4_convolution.pdf")
    plt.show()


if __name__ == '__main__':
    main()
