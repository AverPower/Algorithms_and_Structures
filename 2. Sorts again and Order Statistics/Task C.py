def merge_sort(array, N, rank):
    if N == 1:
        return array
    k = int(N / 2)
    left = array[:k]
    right = array[k:]
    left = merge_sort(left, k, rank)
    right = merge_sort(right, N - k, rank)
    return merge(left,right, rank)

def merge(left, right, rank):
    res = []
    n = len(left)
    m = len(right)
    i = j = 0
    while i + j < n + m:
        if j == m or (i < n and left[i][rank] <= right[j][rank]):
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    return res


n, m, k = list(map(int, input().split()))
array = []
for i in range(n):
    array.append(input())
    
for i in range(k):
    array = merge_sort(array, n, m - i - 1)
print(*array)
