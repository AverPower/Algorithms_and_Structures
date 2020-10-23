from math import inf
from sys import stdin


class LAS:
    def __init__(self, n, seq):
        self.n = n
        self.seq = seq
        self.dp = [1] + [-inf] * (self.n - 1)
        self.index = [-inf] * self.n
    
    def count(self):
        for i in range(1, self.n):
            max_idx = 0
            j = i - 1
            while j != - 1:
                if self.dp[j] > max_idx and self.seq[i] > self.seq[j]:
                    self.index[i] = j
                    max_idx = self.dp[j]
                self.dp[i] = max_idx + 1
                j -= 1
        k, max_end = self.find_max(self.dp)
        subseq = []
        subseq.append(self.seq[max_end])
        while (self.index[max_end] != -inf):
            subseq.append(self.seq[self.index[max_end]])
            max_end = self.index[max_end]
        return k, subseq[::-1]
        
        
    def find_max(self, array):
        m = -inf
        idx = 0
        for i in range(len(array)):
            if array[i] > m:
                idx = i
                m = array[i]
        return m, idx
        
        
args = stdin.readlines()
n = int(args[0])
seq = list(map(int, args[1].split()))

my_las = LAS(n, seq)
k, subseq = my_las.count()
print(k)
print(*subseq)
