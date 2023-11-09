import matplotlib.pyplot as plt
from scipy.signal import tf2zpk
import numpy as np
b = [2, 0.5, 0]
a = [1, -1, -0.75]

# Get the poles and zeros
zeros, poles, _ = tf2zpk(b, a)

# Plot the pole-zero plot
plt.figure()
plt.scatter(np.real(poles), np.imag(poles), marker='x', color='r', label='Poles')
plt.scatter(np.real(zeros), np.imag(zeros), marker='o', color='b', label='Zeros')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.axvline(0, color='k', linestyle='--', linewidth=1)
plt.axhline(0, color='k', linestyle='--', linewidth=1)
plt.grid()
plt.legend()
plt.title('Pole-Zero Plot')
plt.show()