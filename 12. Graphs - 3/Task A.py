class USS:
    def __init__(self, n):
        self.n = n
        self.p = list(range(self.n))
        self.min = list(range(1, self.n + 1))
        self.max = list(range(1, self.n + 1))
        self.count = [1] * self.n
        self.r = [0] * self.n
        
    def get_p(self, x):
        if self.p[x] != x:
            self.p[x] = self.get_p(self.p[x])
        return self.p[x]
    
    def get_all(self, x):
        p = self.get_p(x)
        return self.min[p], self.max[p], self.count[p]
    
    def join(self, x, y):
        x = self.get_p(x)
        y = self.get_p(y)
        if x == y:
            return
        if self.r[x] > self.r[y]:
            x, y = y, x
        if self.r[x] == self.r[y]:
            self.r[y] += 1
        self.p[x] = y
        self.min[y] = min(self.min[x], self.min[y])
        self.max[y] = max(self.max[x], self.max[y])
        self.count[y] += self.count[x]
        
        
n = int(input())
uss = USS(n)
while True:
    try:
        line = input()
        line = line.split()
        if line[0] == "union":
            uss.join(int(line[1]) - 1, int(line[2]) - 1)
        else:
            print(*uss.get_all(int(line[1]) - 1))
    except Exception:
        break
