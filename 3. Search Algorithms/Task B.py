from sys import stdin, stdout

def lower_bound(l, r, x, a):
    if l == r - 1:
        return r
    m = int((l + r) / 2)
    if x <= a[m]:
        return lower_bound(l, m, x, a)
    else:
        return lower_bound(m, r, x, a)
    
def nums_counter(left, right, array, n, bounds_dict):
    right_value = -1
    left_value = -1
    
    if left <= array[0]:
        left_value = 0
    if right >= array[-1]:
        right_value = n

    if right_value == -1:
        right_value = bounds_dict.get(right + 1, -1)
        if right_value == -1:
            right_value = lower_bound(-1, n, right + 1, array)
    if left_value == -1:
        left_value = bounds_dict.get(left, -1)
        if left_value == -1:
            left_value = lower_bound(-1, n, left, array)
    return right_value - left_value


params = stdin.readlines()
n = int(params[0])
array = list(map(int, params[1].split()))
array = sorted(array)
k = int(params[2]) 
bounds_dict = dict()
result = []

for i in params[3:]:
    left, right = map(int, i.split())
    result.append(nums_counter(left, right, array, n, bounds_dict))

stdout.write(" ".join(str(r) for r in result))
