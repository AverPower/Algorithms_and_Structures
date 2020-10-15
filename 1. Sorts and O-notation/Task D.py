def merge_sort(array, N, counter = 0):
    if N == 1:
        return array, counter
    k = int(N / 2)
    left = array[:k]
    right = array[k:]
    left, counter = merge_sort(left, k, counter)
    right, counter = merge_sort(right, N - k, counter)
    res, add = merge(left, right)
    return res, counter + add
 
def merge(left, right):
    res = []
    n = len(left)
    m = len(right)
    i = j = counter = 0
    while i + j < n + m:
        if j == m or (i < n and left[i] < right[j]):
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            counter += n - i
            j += 1       
    return res, counter
 
N = int(input())
array = list(map(int, input().split()))
print(merge_sort(array, N)[1])
