from math import inf
from sys import stdin
class Turtle:
    
    def __init__(self, n, m, coins):
        self.n = n
        self.m = m
        self.coins = coins
        
        self.way = []
        self.field = []
        
        self.way.append([-inf] * (self.m + 1))
        self.field.append([-inf] * (self.m + 1))

        for j in range(self.n):
            self.field.append([-inf] * (self.m + 1))
            self.way.append([-inf] * (self.m + 1))

        self.field[1][1] = self.coins[0][0]
        self.way[1][1] = (0, 0)
        
        
    def count(self):
        for i in range(1, self.n + 1):
            for j in range(1, self.m + 1):
                if i > 1 or j > 1:
                    if self.field[i][j - 1] > self.field[i - 1][j]:
                        self.field[i][j] = self.field[i][j - 1] + self.coins[i - 1][j - 1]
                        self.way[i][j] = (i, j - 1)
                    else:
                        self.field[i][j] = self.field[i - 1][j] + self.coins[i - 1][j - 1]
                        self.way[i][j] = (i - 1, j)
        return self.field[-1][-1]
    
    def get_way(self):
        i = self.n
        j = self.m
        ans = ''
        while i > 0 and j > 0:
            if self.way[i][j][0] < i:
                ans += 'D'
            else:
                ans += 'R'
            i, j = self.way[i][j]
        return ans[-2::-1]
        
        
args = stdin.readlines()
n, m = map(int, args[0].split())
coins = []
for i in range(n):
    coins.append(list(map(int, args[i + 1].split())))
    
my_turtle = Turtle(n, m, coins)

print(my_turtle.count())
print(my_turtle.get_way())
