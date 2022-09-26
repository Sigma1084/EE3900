import numpy as np
from numpy.fft import fft
import matplotlib.pyplot as plt
#If using termux
#import subprocess
#import shlex
#end if

x = np.array([1.0,2.0,3.0,4.0,2.0,1.0])
dft_matrix = fft(np.eye(len(x)))
X = x @ dft_matrix
for x in X:
    print(x)
# print(X)
