def g(max_len, array, k):
    k_count = 0
    for i in array:
        k_count += i//max_len
    return k_count >= k

def lower_bound(left, right, g, k, array):
    if left == right - 1:
        return left
    middle = (left + right) // 2
    
    if g(middle, array, k):
        return lower_bound(middle, right, g, k, array)
    else:
        return lower_bound(left, middle, g, k, array)

n, k = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))

print(lower_bound(0, sum(array)//k + 1, g, k, array))
