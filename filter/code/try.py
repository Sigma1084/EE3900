from sympy import exp, log, symbols, init_printing, lambdify
init_printing(use_latex='matplotlib')

import numpy as np
import matplotlib.pyplot as plt

def _complex_mult(n):
  return n**2.5

def _complex_fft(n):
  return 4*(n**2)*log(n)

def fft_mult_fft(n, m):
  return _complex_fft(n) * 2 + _complex_mult(n)

def conv(n, m):
  return n*n*_complex_mult(m)


n = symbols('n') 
m = symbols('m') 

M = np.linspace(1, 1001, 10)
kernel_size = np.linspace(7, 7, 1)**2

fft_symb = fft_mult_fft(n, m)
discrete_symb = conv(n, m)

fft_func = lambdify(n, fft_symb, 'numpy')
dicrete_func = lambdify([n, m], discrete_symb, 'numpy')


plt.plot(M, fft_func(M), label='fft')
plt.plot(M, dicrete_func(M, kernel_size), label='convolution')
plt.legend()
plt.show()
