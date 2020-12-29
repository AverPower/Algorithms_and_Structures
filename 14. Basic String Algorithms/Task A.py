P = 31
M = 10 ** 20
class String:
    def __init__(self, s):
        n = len(s)
        self.hash = [0] * n
        self.powp = [1] * n
        self.hash[0] = ord(s[0])
        for i in range(1, n):
            self.hash[i] = (self.hash[i - 1] * P + ord(s[i])) % M
            self.powp[i] = (self.powp[i - 1] * P) % M
            
    def getHash(self, l, r):
        if l == 0:
            return self.hash[r]
        return (self.hash[r] - self.hash[l - 1] * self.powp[r - l + 1]) % M
                
    def checkEqual(self, l1, r1, l2, r2):
        if r1 - l1 == r2 - l2:
            if self.getHash(l1, r1) == self.getHash(l2, r2):
                return True
        return False
        
s = input()
string = String(s)
res = []
m = int(input())
for _ in range(m):
    t = list(map(lambda x: int(x) - 1, input().split()))
    res.append(string.checkEqual(*t))
for i in res:
    if i:
        print("Yes")
    else:
        print("No")
