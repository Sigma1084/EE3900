import numpy as np
import matplotlib.pyplot as plt
from scipy import fft

A = 12
f = 50


def c(k: int):
    if k % 2 == 1:
        return 0
    return (2 * A / np.pi) / (1 - k * k)


def main():
    ts = 1e-4
    t = np.arange(-3/f, 3/f, ts)
    scale = t.size / 2

    x = A * np.abs(np.sin(2 * np.pi * f * t))  # Original signal
    x_fft = fft.fft(x)  # fft of x
    sampl_freq = fft.fftfreq(x.size, d=ts)  # Returns the Discrete Fourier Transform sample frequencies.

    plt.plot(sampl_freq, np.abs(x_fft), 'C0.')  # Plot the fft of the original signal
    # Plot the calculated fft
    for k in [-8, -6, -4, -2, 0, 2, 4, 6, 8]:
        plt.plot([f * k, f * k], [0, scale * np.abs(2 * c(k))], 'C1')

    plt.grid()
    plt.xlim(-10*f, 10*f)
    plt.xlabel('f (Hz)')
    plt.ylabel('X(f)')
    plt.legend(['Original', 'Using c(k)'])
    plt.savefig("../figs/Ex3_08_verify_xt_fourier.pdf")
    plt.show()


if __name__ == '__main__':
    main()
