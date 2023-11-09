import numpy as np
import matplotlib.pyplot as plt

N = 10
x = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
DTFS = []
a = -1j
for k in range(0, 50):
    c_k = 0
    for n in range(N):
        c_k += x[n] * np.exp((-1j * 2 * np.pi * k * n)/N)
    c_k /= N
    DTFS.append(c_k)

# Lấy phần thực của hệ số DTFS để vẽ biểu đồ
real_part = [c.real for c in DTFS]

# Tạo mảng tần số k
k_values = np.arange(0,50)

# Vẽ biểu đồ
plt.stem(k_values, real_part)
plt.xlabel('k')
plt.ylabel('Re(c[k])')
plt.title('Biểu đồ DTFS')
plt.show()
