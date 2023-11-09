import numpy as np
import matplotlib.pyplot as plt

def bo_loc_thong_thap(k):
    if k == 0:
        return 1 / 4
    return round(np.sin((k * np.pi) / 4) / (k * np.pi), 4)


def cal_d(M=0):
    result = []
    result_index = []
    if M == 0:
        return result

    N = int(M / 2)
    for i in range(-N, N + 1):
        result.append(bo_loc_thong_thap(i))
        result_index.append(i)
    return result , result_index


result ,result_index = cal_d(M=11)
plt.stem(result_index, result)
plt.xlabel('x')
plt.ylabel('y')
plt.show()