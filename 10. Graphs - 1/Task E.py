from sys import setrecursionlimit
import threading


RECURSION_LIMIT = 10 ** 9
STACK_SIZE = 2 ** 26

setrecursionlimit(RECURSION_LIMIT)
threading.stack_size(STACK_SIZE)


class Graph:
    def __init__(self, g, n):
        self.g = g
        self.tin = [0] * n
        self.up = [0] * n
        self.used = [0] * n
        self.joint_points = set()
        self.time = 1

    def dfs(self, v, parent):
        self.used[v] = 1
        if set([v]) == set(self.g[v]):
            self.joint_points.add(v + 1)
            return
        self.tin[v] = self.time
        self.up[v] = self.tin[v]
        child = 0
        for u in self.g[v]:
            if u != parent:
                if self.used[u] == 0:
                    self.time += 1
                    self.dfs(u, v)
                    self.up[v] = min(self.up[v], self.up[u])
                    child += 1
                    if self.up[u] >= self.tin[v] and parent != None:
                        self.joint_points.add(v + 1)
                else:
                    self.up[v] = min(self.up[v], self.tin[u])
        if parent == None and child >= 2:
            self.joint_points.add(v + 1)

def main():
    n, m = map(int , input().split())
    g = []
    for _ in range(n):
        g.append([])
    for _ in range(m):
        pair = list(map(int, input().split()))
        g[pair[0] - 1].append(pair[1] - 1)
        if pair[0] != pair[1]:
            g[pair[1] - 1].append(pair[0] - 1)

    graph = Graph(g, n)

    for v in range(n):
        graph.dfs(v, None)
    print(len(graph.joint_points))
    print(*sorted(graph.joint_points)) 
    
if __name__ == "__main__":
    threading.Thread(target=main).start()
