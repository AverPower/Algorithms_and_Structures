from math import inf


def add_edge(g, a, b, c, f):
    for i in range(len(g[a])):
        if g[a][i][0] == b:
            g[a][i][1] += c
            for j in range(len(g[b])):
                if g[b][j][0] == a:
                    g[b][j][1] += c
                    break
            break
    else:
        g[a].append([b, c])
        g[b].append([a, c])
        f[(a,b)] = 0
        f[(b,a)] = 0
                   

n = int(input())
m = int(input())
g = []
for _ in range(n):
    g.append([])

f = dict()
    
for _ in range(m):
    line = input().split()
    a = int(line[0]) - 1
    b = int(line[1]) - 1
    c = int(line[2])
    add_edge(g, a, b, c, f)
    

def pushFlow(v, t, curflow, g, used):
    used[v] = 1
    if v == t:
        return curflow
    for edge in g[v]:
        if not used[edge[0]] and f[(v, edge[0])] < edge[1]:
            nextflow = min(curflow, edge[1] - f[(v, edge[0])])
            delta = pushFlow(edge[0], t, nextflow, g, used)
            if delta > 0:
                f[(v, edge[0])] += delta
                f[(edge[0], v)] -= delta
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

print(ans)
