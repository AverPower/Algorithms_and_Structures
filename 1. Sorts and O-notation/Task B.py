def sort_bubble(array, N):
    for i in range(N - 1):
        for j in range(N - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array
    
N = int(input())
array = list(map(int, input().split()))
print(*sort_bubble(array, N))
