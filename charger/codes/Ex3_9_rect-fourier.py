import numpy as np
import matplotlib.pyplot as plt
from scipy import fft


def main():
    ts = 1e-2  # Step size
    t = np.arange(-1, 1, ts)
    scale = t.size / 2
    fft.fftshift()

    # Using x = rect(t)
    rect = np.logical_and(-0.5 <= t, t <= 0.5).astype(int)  # Original signal
    x_fft = fft.fft(rect)  # fft of x
    sampl_freq = fft.fftfreq(rect.size, d=ts)  # Returns the Discrete Fourier Transform sample frequencies.

    plt.plot(sampl_freq, np.abs(x_fft), 'C0.')
    plt.plot(sampl_freq, np.sin(np.pi * sampl_freq) / (np.pi * sampl_freq), 'C1')

    plt.grid()
    plt.xlabel('f (Hz)')
    plt.ylabel(r'$\mathcal{F}(rect t) (f)$')
    plt.legend(['Original', 'Using c(k)'])
    # plt.savefig("../figs/Ex3_8_verify_xt_fourier.pdf")
    plt.show()


if __name__ == '__main__':
    main()
