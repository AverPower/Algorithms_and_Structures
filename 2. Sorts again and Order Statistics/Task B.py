array = list(map(int, input().split()))

cnt = dict()
for i in range(len(array)):
    if cnt.get(array[i], 0):
        cnt[array[i]] += 1
    else:
        cnt[array[i]] = 1

i = 0
for j in range(0, 101):
    while cnt.get(j, 0):
        array[i] = j
        i += 1
        cnt[j] -= 1

print(*array)
