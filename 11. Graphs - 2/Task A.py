from queue import Queue

class Knight:
    
    def __init__(self, n, s):
        self.n = n
        self.s = s
        self.used = []
        self.d = []
        self.way = []
        for _ in range(self.n):
            self.used.append([0] * self.n)
            self.d.append([0] * self.n)
            self.way.append([0] * self.n)
        self.used[s[0] - 1][s[1] - 1] = 1
        
    def generate_points(self, s):
        res = []
        oper_1 = [1, -1]
        oper_2 = [2, -2]
        for o_1 in oper_1:
            for o_2 in oper_2:
                if 0 < s[0] + o_1 < self.n + 1 and 0 < s[1] + o_2 < self.n + 1: 
                    res.append((s[0] + o_1, s[1] + o_2))
                if 0 < s[0] + o_2 < self.n + 1 and 0 < s[1] + o_1 < self.n + 1:     
                    res.append((s[0] + o_2, s[1] + o_1))
        return res
    
    def bfs(self):
        queue = Queue()
        queue.put(self.s)
        while not queue.empty():
            v = queue.get()
            for u in self.generate_points(v):
                if not self.used[u[0] - 1][u[1] - 1]:
                    self.used[u[0] - 1][u[1] - 1] = 1
                    queue.put(u)
                    self.d[u[0] - 1][u[1] - 1] = self.d[v[0] - 1][v[1] - 1] + 1
                    self.way[u[0] - 1][u[1] - 1] = (v[0] - 1, v[1] - 1)        
    
    def generate_route(self, point):
        self.route = []
        cur_point = (point[0] - 1, point[1] - 1)
        while cur_point != 0:
            self.route.append((cur_point[0] + 1, cur_point[1] + 1))
            cur_point = self.way[cur_point[0]][cur_point[1]]
        self.route.reverse()
    
    def print_result(self, point):
        self.generate_route(point)
        print(self.d[point[0] - 1][point[1] - 1] + 1)
        for r in self.route:
            print(*r)
            
n = int(input())
s = tuple(map(int, input().split()))
point = tuple(map(int, input().split()))

knight = Knight(n, s)
knight.bfs()
knight.print_result(point)
