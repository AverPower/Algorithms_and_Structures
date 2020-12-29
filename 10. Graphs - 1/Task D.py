from sys import setrecursionlimit
import threading


RECURSION_LIMIT = 10 ** 9
STACK_SIZE = 2 ** 26

setrecursionlimit(RECURSION_LIMIT)
threading.stack_size(STACK_SIZE)


def dfs(v, used, g, answer):
    used[v] = 1
    for u in g[v]:
        if used[u] == 0:
            dfs(u, used, g, answer)
    answer.append(v)

def dfs_2(v, color, cur, g_back):
    color[v] = cur
    for u in g_back[v]:
        if color[u] == 0:
            dfs_2(u, color, cur, g_back)

def main():
    n, m = map(int , input().split())
    g = []
    g_back = []
    for _ in range(n):
        g.append([])
        g_back.append([])
        
    for _ in range(m):
        pair = list(map(int, input().split()))
        g[pair[0] - 1].append(pair[1] - 1)
        g_back[pair[1] - 1].append(pair[0] - 1)
    
    used = [0] * n
    color = [0] * n
    answer = []

    for v in range(n):
        if used[v] == 0:
            dfs(v, used, g, answer)
    answer.reverse()

    cnt = 0
    for v in answer:
        if color[v] == 0:
            cnt += 1
            dfs_2(v, color, cnt, g_back)
    
    ribs = []
    for _ in range(max(color)):
        ribs.append(set())
    
    for v in range(n):
        for u in g[v]:
            if color[v] != color[u]:
                ribs[color[v]].add(color[u])
    
    result = 0
    for r in ribs:
        result += len(r)
    print(result)
    
if __name__ == "__main__":
    threading.Thread(target=main).start()
