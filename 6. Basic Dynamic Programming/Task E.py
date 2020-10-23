from sys import stdin

from math import inf

class Cafe:
    def __init__(self, n, cost):
        self.n = n
        self.cost = [0] + cost
        d = [[0] + (self.n + 1) * [inf]]
        for i in range(self.n):
            d.append( (self.n + 2) * [inf])
        self.d = d
        self.way = [(self.n + 1) * [inf] for _ in range(self.n + 1)]
        
    def calculate_d(self):
        for i in range(1, self.n + 1):
            for j in range(self.n + 1):

                if self.cost[i] > 100 and j != 0:
                    if j != 0:
                        if self.d[i - 1][j - 1] + self.cost[i] <= self.d[i - 1][j + 1]:
                            self.d[i][j] = self.d[i - 1][j - 1] + self.cost[i]
                            self.way[i][j] = (i - 1, j - 1)
                        else:
                            self.d[i][j] = self.d[i - 1][j + 1]
                            self.way[i][j] = (i - 1, j + 1)
                else:
                    if self.d[i - 1][j] + self.cost[i] <= self.d[i - 1][j + 1]:
                        self.d[i][j] = self.d[i - 1][j] + self.cost[i]
                        self.way[i][j] = (i - 1, j)
                    else:
                        self.d[i][j] = self.d[i - 1][j + 1]
                        self.way[i][j] = (i - 1, j + 1)
        
        
    def count(self):
        if self.n == 0:
            return 0, 0, []
        self.calculate_d()
        idx = 0
        minimum = inf
        for j in range(self.n + 2):
            if self.d[-1][j] <= minimum:
                minimum = self.d[-1][j]
                idx = j
        
        res = []
        k = self.way[-1][idx]
        res.append(idx)
        while k[0] != 0:
            res.append(k[1])
            k = self.way[k[0]][k[1]]
        res = [0] + res[::-1]
        
        days = []
        for i in range(len(res) - 1):
            if res[i + 1] < res[i]:
                days.append(i + 1)
                
        return minimum, idx, days
        
        
args = stdin.readlines()
n = int(args[0])
a = list(map(lambda x: int(x.strip()), args[1:]))
my_cafe = Cafe(n, a)
result = my_cafe.count()
print(result[0])
print(result[1], len(result[2]))
for i in result[2]:
    print(i)
