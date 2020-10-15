def bin_search(left, right, query, array):
    if left == right - 1:
        if abs(array[left] - query) <= abs(array[right] - query):
            return array[left]
        else:
            return array[right]
    
    middle = (left + right) // 2
    if query == array[middle]:
        return array[middle]

    if query < array[middle]:
        return bin_search(left, middle, query, array)
    else:
        return bin_search(middle, right, query, array)

n, m = map(int, input().split())
array_base = list(map(int, input().split()))
array_query = list(map(int, input().split()))


for query in array_query:
    print(bin_search(0, n - 1, query, array_base))
