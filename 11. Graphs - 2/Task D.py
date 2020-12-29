from math import inf
from sys import setrecursionlimit
import threading


RECURSION_LIMIT = 10 ** 9
STACK_SIZE = 2 ** 26

setrecursionlimit(RECURSION_LIMIT)
threading.stack_size(STACK_SIZE)

def dfs(v, color, cur, g):
    color[v] = cur
    for u in g[v]:
        if color[u] == 0:
            dfs(u, color, cur, g)

def main():

    n, m, s = map(int, input().split())
    s -= 1
    edges = []
    weights = []
    parent = [-1] * n
    d = [inf] * n
    d[s] = 0
    g = []
    for _ in range(n):
        g.append([])
    
    for _ in range(m):
        nums = list(map(int, input().split()))
        edges.append((nums[0] - 1, nums[1] - 1))
        g[nums[0] - 1].append(nums[1] - 1)
        weights.append(nums[2])

    for _ in range(n - 1):
        for i, edge in enumerate(edges):
            if d[edge[0]] < inf:
                if d[edge[1]] > d[edge[0]] + weights[i]:
                    d[edge[1]] = max(-inf, d[edge[0]] + weights[i])
                    parent[edge[1]] = edge[0]
    
    bad_vertex = []
    
    for i, edge in enumerate(edges):
        if d[edge[0]] < inf:
            if d[edge[1]] > d[edge[0]] + weights[i]:
                cur = edge[1]
                bad_vertex.append(cur)
                for _ in range(n):
                    cur = parent[cur]
                    bad_vertex.append(cur)
                    
    bad_vertex = set(bad_vertex)

    cnt = 0
    color = [0] * n
    for v in bad_vertex:
        if color[v] == 0:
            cnt += 1
            dfs(v, color, cnt, g)
            
    bad_colors = set()
    for vertex in bad_vertex:
        bad_colors.add(color[vertex])
    
    for i in range(n):
        if d[i] == inf:
            print("*")
        else:
            if color[i] in bad_colors:
                print("-")
            else:
                print(d[i])
            
if __name__ == "__main__":
    threading.Thread(target=main).start()
