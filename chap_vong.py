import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
x1 = [2, 3, 4, 0]


def fourier_reverse(x_arg):
    x_reverse = x_arg[::-1]
    return [x_arg[0]] + x_reverse[:len(x_reverse) - 1]


def fourier_move(x_arg, move_arg):
    return x_arg[len(x_arg) - move_arg:] + x_arg[:len(x_arg) - move_arg]


xm_reverse = fourier_reverse(x)
xm_arr = []
for n in range(0, 4):
    xm_arr.append(fourier_move(xm_reverse, n))

x1_np = np.array(x1)
x1_n = []
y1_n = []
for index,e in enumerate(xm_arr):
    x1_n.append(index)
    n = np.dot(x1_np , np.array(e))
    y1_n.append(n)
    print("n={}: {}".format(index,n))

plt.stem(x1_n, y1_n)
plt.xlabel('x')
plt.ylabel('y')
plt.title("Chập vòng")
plt.show()