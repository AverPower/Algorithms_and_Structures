from sys import setrecursionlimit
import threading


RECURSION_LIMIT = 10 ** 9
STACK_SIZE = 2 ** 24

setrecursionlimit(RECURSION_LIMIT)
threading.stack_size(STACK_SIZE)


def dfs(v, used, counter, g):
    used[v] = 1
    for u in g[v]:
        if not used[u]:
            counter[u] = counter[v] + 1
            dfs(u, used, counter, g)

def main():
    m = int(input())
    users = []
    logs = []
    
    for _ in range(m):
        line = list(map(lambda x: x.lower(), input().split()))
        logs.append((line[0], line[2]))
        if line[2] not in users:
            users.append(line[2])
        if line[0] not in users:
            users.append(line[0])
            
    n = len(users)
    g = []
    for _ in range(n):
        g.append([])
    
    for line in logs:
        g[users.index(line[1])].append(users.index(line[0])) 
    
    counter = [0] * n
    used = [0] * n
    
    for v in range(n):
        if used[v] == 0:
            dfs(v, used, counter, g)

    print(max(counter) + 1)
    
if __name__ == "__main__":
    threading.Thread(target=main).start()
