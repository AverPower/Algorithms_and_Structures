from sys import setrecursionlimit
import threading


RECURSION_LIMIT = 10 ** 9
STACK_SIZE = 2 ** 26

setrecursionlimit(RECURSION_LIMIT)
threading.stack_size(STACK_SIZE)


def dfs(v, color, g, answer):
    color[v] = 1
    for u in g[v]:
        if color[u] == 0:
            dfs(u, color, g, answer)
        if color[u] == 1:
            return 1
    answer.append(v + 1)
    color[v] = 2
    return None

def main():
    n, m = map(int , input().split())
    g = []
    for _ in range(n):
        g.append([])
    
    for _ in range(m):
        pair = list(map(int, input().split()))
        g[pair[0] - 1].append(pair[1] - 1)
   
    color = [0] * n
    cycle = 0
    answer = []
    for v in range(n):
        if color[v] == 0:
            if dfs(v, color, g, answer) == 1:
                cycle = 1
                break          
    if cycle:
        print(-1)
    else:
        answer.reverse()
        print(*answer)
    
if __name__ == "__main__":
    threading.Thread(target=main).start()
