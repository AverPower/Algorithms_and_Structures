from math import inf

def add_edge(g, a, b, c, f, cap):
    g[a].append(b)
    g[b].append(a)
    f[(a, b)] = 0
    f[(b, a)] = 0
    cap[(a, b)] = c
    cap[(b, a)] = c
    
def dfs(v, color, cur):
    color[v] = cur
    for u in g_left[v]:
        if color[u] == 0:
            dfs(u, color, cur)
                   

n, m = map(int, input().split())
g = []
for _ in range(n):
    g.append([])

f = dict()
cap = dict()
color = dict()
edges = []
for _ in range(m):
    line = input().split()
    a = int(line[0]) - 1
    b = int(line[1]) - 1
    c = int(line[2])
    add_edge(g, a, b, c, f, cap)
    edges.append((a, b))
    
    
def pushFlow(v, t, curflow, g, used):
    used[v] = 1
    if v == t:
        return curflow
    
    for u in g[v]:
        if not used[u] and f[(v, u)] < cap[(v, u)]:
            nextflow = min(curflow, cap[(v, u)] - f[(v, u)])
            delta = pushFlow(u, t, nextflow, g, used)
            if delta > 0:
                f[(v, u)] += delta
                f[(u, v)] -= delta
                return delta
    return 0

ans = 0
while True:
    used = [0] * n
    delta = pushFlow(0, n - 1, inf, g, used)
    if delta > 0:
        ans += delta
    else:
        break

g_left = []
for _ in range(n):
    g_left.append([])

for edge in cap:
    if cap[edge] - f[edge] > 0:
        g_left[edge[0]].append(edge[1])
        
cnt = 0
color = [0] * n
for v in range(n):
    if color[v] == 0:
        cnt += 1
        dfs(v, color, cnt)
        
cut = set()
for i in range(n):
    if color[i] == 1:
        for j in g[i]:
            if color[j] != 1:
                cut.add((i, j))
                
idx = []
for i, edge in enumerate(edges):
    if edge in cut or edge[::-1] in cut:
        idx.append(i + 1)
        
print(len(cut), ans)
print(*idx)
