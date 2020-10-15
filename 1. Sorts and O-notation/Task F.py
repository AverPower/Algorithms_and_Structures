def roman_to_arabic(num):
    r_to_a = {'I': 1, 'V': 5, 'X': 10, 'L': 50}
    last = num[-1]
    result = r_to_a[last]
    for i in num[-2::-1]:
        if r_to_a[i] >= r_to_a[last]:
            result += r_to_a[i]
        else:
            result -= r_to_a[i]
        last = i
    return result   

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
            i += 1
        else:
            res.append(right[j])
            j += 1
    return res

def arabic_to_roman(num):
    low = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
    high = ["","X","XX","XXX","XL","L"]
    return high[num // 10 % 10] + low[num % 10]

N = int(input())
array = []
for i in range(N):
    name, num = input().split()
    array.append((name, roman_to_arabic(num)))

for res in merge_sort(array, N):
    print(f'{res[0]} {arabic_to_roman(res[1])}')
