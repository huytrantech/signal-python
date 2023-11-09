import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz
M = 61
wc = np.pi / 3

# Vẽ |H(k)|
h = np.zeros(M)
n = np.arange(-M//2 + 1, M//2 + 1)

h = np.sin(wc * n) / (np.pi * n)
h[M//2] = wc / np.pi
print(h)

plt.figure(figsize=(10, 5))
plt.stem(n + M // 2, h) 
plt.title('Impulse response')
plt.xlabel('n')
plt.ylabel('h(n)')
plt.grid()
plt.show()

# Vẽ phổ |H(k)|
w, H = freqz(h)
plt.figure(figsize=(10, 5))
plt.plot(w, np.abs(H))
plt.title('Frequency response')
plt.xlabel('w')
plt.ylabel('|H(w)|')
plt.grid()
plt.show()