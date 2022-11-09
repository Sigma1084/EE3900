import numpy as np
import matplotlib.pyplot as plt
from scipy import fft


def main():
    ts = 1e-2  # Sampling period
    signal = np.zeros(200)  # Signal
    signal[:100] = 1
    sig_fft = fft.fftshift(fft.fft(signal))
    sig_fft = np.abs(sig_fft) / max(np.abs(sig_fft))
    sf = fft.fftshift(fft.fftfreq(signal.size, d=ts))
    plt.plot(sf, sig_fft, '.', label='Simulation')
    plt.plot(sf, np.sinc(sf), label='Analysis')
    plt.legend()
    plt.grid()
    plt.xlabel('f (Hz)')
    plt.ylabel('H(f)')
    plt.savefig("../figs/Ex3_09_verify_rect_fourier.pdf")
    plt.show()


if __name__ == '__main__':
    main()
