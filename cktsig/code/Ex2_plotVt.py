# Path: cktsig/code/Ex2_plotVn.py
import numpy as np
from matplotlib import pyplot as plt


def vt(t: float):
	if t <= 0:
		return 0
	return (4 / 3) * (1 - np.exp(-1.5 * 10 ** 6 * t))


def main():
	num_vt = np.vectorize(vt, otypes=['double'])
	vc1 = np.loadtxt('Ex2_output.dat', dtype='double')
	t = np.linspace(0, 5e-6, 10000)
	V_calc = num_vt(t)
	plt.plot(t, V_calc, label='Calculated')
	plt.plot(vc1[:, 0], vc1[:, 1], '.', label='Simulated(ngspice)', color='red')
	plt.xlabel('t (s)')
	plt.ylabel('$v_{c_0}(t)$ (V)')
	plt.grid()
	plt.legend()
	plt.plot()
	plt.savefig('../figs/Ex2_vt.pdf')
	plt.show()


if __name__ == '__main__':
	main()
