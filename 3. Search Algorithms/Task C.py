from math import log2

R_BOUND = 10 ** 10
EPS = 10 ** (-7)
ITL = int(log2(R_BOUND / EPS))

def bin_search(left, right, f, c, bound):
    for i in range(bound):
        middle = (left + right)/2
        if f(middle) < c:
            left = middle
        else:
            right = middle
    return right

def f(x):
    return x ** 2 + x ** (1/2)

c = float(input())
print(bin_search(0, R_BOUND, f, c, ITL))
