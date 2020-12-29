from sys import setrecursionlimit
import threading


RECURSION_LIMIT = 10 ** 9
STACK_SIZE = 2 ** 24

setrecursionlimit(RECURSION_LIMIT)
threading.stack_size(STACK_SIZE)

def dfs(v, color, cur, g):
    color[v] = cur
    for u in g[v]:
        if color[u] == 0:
            dfs(u, color, cur, g)

def main():
    n, m = map(int, input().split())
    g = []
    for _ in range(n):
        g.append([])
    
    color = [0] * n
    
    for _ in range(m):
        pair = list(map(int, input().split()))
        g[pair[0] - 1].append(pair[1] - 1)
        g[pair[1] - 1].append(pair[0] - 1)

    cnt = 0
    for v in range(n):
        if color[v] == 0:
            cnt += 1
            dfs(v, color, cnt, g)
    print(cnt)
    print(*color)
    
if __name__ == "__main__":
    threading.Thread(target=main).start()
