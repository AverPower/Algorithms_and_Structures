from random import choice

def quick_sort(array, N):
    if N == 1:
        return array
    if N == 0:
        return []
    x = choice(array)
    l, m, r = split(array, x)
    return quick_sort(l, len(l)) + m + quick_sort(r, len(r))

def split(array, x):
    left = []
    right = []
    middle = []
    for i in array:
        if i < x:
            left.append(i)
        elif i == x:
            middle.append(i)
        else:
            right.append(i)
    return left, middle, right

N = int(input())
array = list(map(int, input().split()))
print(*quick_sort(array, N))
