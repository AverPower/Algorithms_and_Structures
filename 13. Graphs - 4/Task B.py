from queue import Queue
from math import inf
 
def add_edge(g, a, b, c, f, cap):
    for i in g[a]:
        if i == b:
            cap[(a, b)] += c
            for j in g[b]:
                if j == a:
                    cap[(b, a)] += c
                    break
            break
    else:
        g[a].append(b)
        g[b].append(a)
        f[(a, b)] = 0
        f[(b, a)] = 0
        cap[(a, b)] = c
        cap[(b, a)] = c
                   
 
n = int(input())
m = int(input())
g = []
for _ in range(n):
    g.append([])
 
f = dict()
cap = dict()
edges = []
for _ in range(m):
    line = input().split()
    a = int(line[0]) - 1
    b = int(line[1]) - 1
    c = int(line[2])
    add_edge(g, a, b, c, f, cap)
    edges.append((a, b, c))
 
 
u = max(cap.values())
delta = 1
while 2 * delta < u:
    delta = 2 * delta
s = 0
t = n - 1
while delta >= 1:
    queue = Queue()
    queue.put(s)
    way = [-1] * n
    way[s] = s
    used = [0] * n
    while not queue.empty():
        v = queue.get()
        if v == t:
            break
        for u in g[v]:
            if not used[u] and cap[(v, u)] - f[(v, u)] >= delta:
                used[u] = 1
                queue.put(u)
                way[u] = v   

    if way[-1] == -1:
        delta = delta // 2
        continue

    cur = t
    curflow = inf
    while cur != s:
        curflow = min(curflow, cap[(way[cur], cur)] - f[(way[cur], cur)])
        cur = way[cur]

    cur = t
    while cur != s:
        f[(way[cur], cur)] += curflow
        f[(cur, way[cur])] -= curflow
        cur = way[cur] 

f_max = 0
for v in g[s]:
    f_max += f[(s, v)]
print(f_max)

for a, b, c in edges:
    flow = f[(a, b)]
    val = min(c, abs(flow))
    res = val if flow >= 0 else -val
    f[(a, b)] -= res
    f[(b, a)] += res
    print(res)
