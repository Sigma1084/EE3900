import numpy as np
from scipy import fft
from matplotlib import pyplot as plt


def main():
    rect = np.vectorize(lambda x: 1 if (np.abs(x) <= 0.5) else 0, otypes=['double'])
    ts = 2e-4
    N = 100
    mid = int(N/ts)
    sig = np.sinc(np.arange(-N, N, ts))
    sig_fft = fft.fftshift(fft.fft(sig))
    sig_fft = np.abs(sig_fft)/np.abs(sig_fft[mid])
    sf = fft.fftshift(fft.fftfreq(sig.size, d=ts))
    plt.plot(sf, sig_fft, '.')
    plt.plot(sf, rect(sf))
    plt.legend(['Simulation', 'Analysis'])
    plt.grid()
    plt.xlim(-2, 2)
    plt.xlabel('f (Hz)')
    plt.ylabel('H(f)')
    plt.savefig("../figs/Ex3_10_verify_sinc_fourier.pdf")
    plt.show()


if __name__ == '__main__':
    main()
