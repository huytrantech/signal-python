import numpy as np
import matplotlib.pyplot as plt


def fft_times():
    # Dãy x
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8], dtype=complex)

    # Sử dụng hàm FFT trong NumPy
    X = np.fft.fft(x)

    # In kết quả
    print("FFT của x:", X)

def fft_frequence():

    x = np.array([1,2,3,4,5,6,7,8])

    fft_result = np.fft.fft(x)
    print(fft_result)

    N = len(x)
    fs = 1
    frequencies = np.fft.fftfreq(N, 1 / fs)

    # Vẽ biểu đồ biên độ
    plt.figure(figsize=(10, 4))
    plt.stem(frequencies, np.abs(fft_result))
    plt.xlabel('Tần số (Hz)')
    plt.ylabel('Biên độ')
    plt.grid(True)
    plt.show()

def fft_radix2(x):
  n = len(x)
  if n == 1:
    return x
  else:
    even = fft_radix2(x[::2])
    odd = fft_radix2(x[1::2])
    out = np.empty(n)
    for k in range(n):
      out[k] = even[k] + np.exp(-2j * np.pi * k / n) * odd[k]
    return out
def fft2():
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    y = fft_radix2(x)
    print(y)

fft2()