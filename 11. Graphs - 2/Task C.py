from math import inf
NO_EDGE_IND = 100000


n = int(input())
a = []

for _ in range(n):
    temp = []
    for num in map(int, input().split()):
        if num == NO_EDGE_IND:
            temp.append(inf)
        else:
            temp.append(num)
    a.append(temp)
    
d = a.copy()
next_matr = []
for _ in range(n):
    next_matr.append(list(range(n)))

for k in range(n):
    for u in range(n):
        for v in range(n):
            if d[u][v] > d[u][k] + d[k][v]:
                d[u][v] = max(-inf, d[u][k] + d[k][v])
                next_matr[u][v] = next_matr[u][k]
              
cycle_vertex = -1 
for i in range(n):
    if d[i][i] < 0:
        cycle_vertex = i
        break

if cycle_vertex != -1:
    cycle = []
    cycle.append(cycle_vertex + 1)
    cur = next_matr[cycle_vertex][cycle_vertex]
    while cur != cycle_vertex:
        if cur + 1 in cycle:
            idx = cycle.index(cur + 1)
            cycle = cycle[idx:]
            break
        cycle.append(cur + 1)
        cur = next_matr[cur][cycle_vertex]
    print("YES")
    print(len(cycle))
    print(*cycle)
else:
    print("NO")
