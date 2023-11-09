import numpy as np
import matplotlib.pyplot as plt

def dot_arr(x, y):
    return np.dot(x, y)


def move_vector(x, ind, value):
    if value == 0:
        return ind, x

    if value > 0:
        for i in range(value):
            if ind != 0:
                ind -= 1
            else:
                x = [0] + x

    if value < 0:
        for i in range(-value):
            if ind < len(x):
                ind += 1
            if ind >= len(x):
                x = x + [0]

    if ind >= len(x):
        ind = len(x) - 1
    if ind <= 0:
        ind = 0

    return ind, x


def conv_signal(arr_1, index1, arr_2, index2):

    right1 = np.array(arr_1[index1:])
    right2 = np.array(arr_2[index2:])
    max_length = max(len(right1), len(right2))
    right1_init = np.zeros(max_length)
    right2_init = np.zeros(max_length)
    right1_init[:len(right1)] = right1
    right2_init[:len(right2)] = right2

    left1 = np.array(arr_1[:index1])[::-1]
    left2 = np.array(arr_2[:index2])[::-1]
    max_length = max(len(left1), len(left2))
    left1_init = np.zeros(max_length)
    left2_init = np.zeros(max_length)
    left1_init[:len(left1)] = left1
    left2_init[:len(left2)] = left2
    #
    # print(right1_init)
    # print(right2_init)
    # print(left1_init)
    # print(left2_init)

    return np.dot(right1_init, right2_init) + np.dot(left1_init, left2_init)


def reverse(y, point):
    index = 0
    for i, v in enumerate(y):
        if v == point:
            index = i
            break

    return y[index + 1:][::-1] + [y[index]] + y[:index][::-1]


vector_reverse = reverse([1, 3, -3, 4], 4)
result = []
result_n = []
for i in range(-5, 5):
    index, vector_h = move_vector(vector_reverse, 0, i)
    result_n.append(i)
    result.append(conv_signal(vector_h, index,[2,3,4],1))

print(result)
plt.stem(result_n, result)
plt.xlabel('x')
plt.ylabel('y')
plt.show()