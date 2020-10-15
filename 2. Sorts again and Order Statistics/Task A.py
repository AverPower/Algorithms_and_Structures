from random import choice

def quick_sort_modify(array, n, k):
    
    if n == 1:
        return array[k]
    if n == 0:
        return []
    
    x = choice(array)
    a = split(array, x)
    
    left, middle, right = a
    l, m, r = list(map(len, a))

    if k < l:
        return quick_sort_modify(left, l, k)
    
    elif k >= l + m:
        return quick_sort_modify(right, r, k - l - m)
    
    else:
        return middle[0]

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


n = int(input())
clones = list(map(int, input().split()))
m = int(input())
for l in range(m):
    i, j, k = list(map(lambda x: int(x) - 1, input().split()))
    print(quick_sort_modify(clones[i : j + 1], j + 1 - i, k))
