from math import log2

EPS = 0.000001
ITN = int(log2(1 / EPS) / log2(3 / 2))

def h(v_p, v_f, a, x):
    return (((1 - a) ** 2 + x ** 2) ** (1/2)) / v_p  + (((1 - x) ** 2 + a ** 2) ** (1 / 2)) / v_f

def ternary_search(left, right, v_p, v_f, a, bound):
    for i in range(bound):
        middle_1 = (2 * left + right) / 3
        middle_2 = (left + 2 * right) / 3
        if h(v_p, v_f, a, middle_1) < h(v_p, v_f, a, middle_2):
            right = middle_2
        else:
            left = middle_1
    return right

v_p, v_f = map(int, input().split())
a = float(input())

print(ternary_search(0, 1, v_p, v_f, a, ITN))
