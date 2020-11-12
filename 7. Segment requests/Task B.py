from math import inf

A_0 = 23
A_1 = 21563
A_2 = 16714589
L_0 = 17
L_1 = 751
L_2 = 2
R_0 = 13
R_1 = 593
R_2 = 5

class SparseTable:
    def __init__(self, a, n):
        self.logs = self.calc_logs(n)
        self.n = n
        k = self.logs[n] + 1    
    
        self.mins = [ [inf] * k]
        for i in range(n - 1):
            self.mins.append([inf] * k)
            
        for i in range(n):
            self.mins[i][0] = a[i]
            
        for j in range(1, k):
            for i in range(n):
                if (i + 2 ** (j - 1)) < n:
                    self.mins[i][j] = min(self.mins[i][j - 1], self.mins[i + 2 ** (j - 1)][j - 1])
    
    def calc_logs(self, n):
        logs = []
        for i in range(1, n + 2):
            k = 0
            while 2 ** k < i:
                k += 1
            logs.append(max(0, k - 1))
        return logs
        
    
    def calculate_queries(self, m, l, r):
        for i in range(1, m + 1):
            l_t, r_t = min(l,r), max(l,r)
            k = self.logs[r_t - l_t + 1]
            res = min(self.mins[l_t - 1][k], self.mins[r_t - 2**k][k])
            prev = [l, r, res]
            l = (L_0 * l + L_1 + res + L_2 * i) % self.n + 1
            r = (R_0 * r + R_1 + res + R_2 * i) % self.n + 1
        return prev
        
n, m, a_1 = map(int, input().split())
l, r = map(int, input().split())

a = [a_1]
for i in range(1, n):
    a.append((A_0 * a[-1] + A_1) % A_2)

spr_table = SparseTable(a, n)

print(*spr_table.calculate_queries(m, l, r))
