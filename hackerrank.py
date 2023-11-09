import numpy as np


def queensAttack(n, k, r_q, c_q, obstacles):
    arr_attack = []

    top_left_moves = min(n - r_q, c_q - 1)
    top_right_moves = min(n - r_q, n - c_q)
    bottom_right_moves = min(r_q - 1, n - c_q)
    bottom_left_moves = min(r_q - 1, c_q - 1)

    edge = {
        "top_left_edge": n+1,
        "top_right_edge": n+1,
        "bottom_left_edge": 0,
        "bottom_right_edge": 0
    }

    attack_moves = (n - 1) * 2

    for element in obstacles:
        if element[0] == r_q:
            if element[1] < c_q:
                attack_moves -= element[1]
            if element[1] > c_q:
                attack_moves -= (n - element[1]) + 1

        elif element[1] == c_q:
            if element[0] < r_q:
                attack_moves -= element[0]
            if element[0] > r_q:
                attack_moves -= (n - element[0]) + 1

        elif abs(element[0] - r_q) / abs(element[1] - c_q) == 1:
            if element[1] < c_q:
                if r_q < element[0] < edge["top_left_edge"] :
                    edge["top_left_edge"] = element[0]
                elif r_q > element[0] > edge["bottom_left_edge"]:
                    edge["bottom_left_edge"] = element[0]
            elif element[1] > c_q:
                if r_q < element[0] < edge["top_right_edge"]:
                    edge["top_right_edge"] = element[0]
                elif r_q > element[0] > edge["bottom_right_edge"]:
                    edge["bottom_right_edge"] = element[0]

    if edge["bottom_left_edge"] != 0:
        bottom_left_moves = r_q - edge["bottom_left_edge"] - 1
    if edge["bottom_right_edge"] != 0:
        bottom_right_moves = r_q - edge["bottom_right_edge"] - 1
    if edge["top_left_edge"] != n + 1:
        top_left_moves = abs(r_q - edge["top_left_edge"]) - 1
    if edge["top_right_edge"] != n + 1:
        top_right_moves = abs(r_q - edge["top_right_edge"]) - 1

    attack_moves += top_left_moves + top_right_moves + bottom_right_moves + bottom_left_moves
    return attack_moves


print(queensAttack(7, 8, 4, 3, [
    [6, 1],
    [4, 1],
    [2, 1],
    [6,3],
    [1,3],
    [6,5],
    [4,7],
    [1,6]
]))
