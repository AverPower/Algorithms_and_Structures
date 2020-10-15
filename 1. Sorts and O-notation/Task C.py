def merge_sort(array, N):
    if N == 1:
        return array
    k = int(N / 2)
    left = array[:k]
    right = array[k:]
    left = merge_sort(left, k)
    right = merge_sort(right, N - k)
    return merge(left,right)

def merge(left, right):
    res = []
    n = len(left)
    m = len(right)
    i = j = 0
    while i + j < n + m:
        if j == m or (i < n and left[i] < right[j]):
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    return res

N = int(input())
array = list(map(int, input().split()))
print(*merge_sort(array, N))
