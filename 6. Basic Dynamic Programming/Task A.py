from math import inf
from sys import stdin, stdout
from math import inf
class Grasshopper:
    
    def __init__(self, n, k, money):
        self.money = [0] + money + [0]
        self.n = n
        self.k = k
        self.jumps = 0
        self.columns = [0] * self.n 
        self.result = [0] + [-inf] * (n - 1) 
        
    def set_columns_and_jumps(self):
        cols = []
        k = self.columns[-1]
        while k != 0:
            self.jumps += 1
            cols.append(k)
            k = self.columns[k]
        self.columns = [1] + [x + 1 for x in cols][::-1] + [self.n] 
        self.jumps += 1
    
        
    def counter(self):
        for i in range(1, n):
            prev_max = i - 1
            j = max(0, i - k)
            while j <= i - 1:
                if self.result[j] > self.result[prev_max]: 
                    prev_max = j
                self.result[i] = self.result[prev_max] + self.money[i]
                self.columns[i] = prev_max
                j += 1
        return self.result[-1]
    
args = stdin.readlines()
n, k = map(int, args[0].split())
money = list(map(int, args[1].split()))

gs = Grasshopper(n, k, money)

print(gs.counter())
gs.set_columns_and_jumps()
print(gs.jumps)
print(*gs.columns)
