from sys import stdout, stdin
from io import IOBase, BytesIO
from os import read, write, fstat

BUFSIZE = 8192

class FastIO(IOBase):
    newlines = 0
 
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
 
    def read(self):
        while True:
            b = read(self._fd, max(fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
 
    def readline(self, size: int = ...):
        while self.newlines == 0:
            b = read(self._fd, max(fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
 
    def flush(self):
        if self.writable:
            write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)
 
 
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")
 
 
def print(*args, **kwargs):
    sep, file = kwargs.pop("sep", " "), kwargs.pop("file", stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        file.write(str(x))
        at_start = False
    file.write(kwargs.pop("end", "\n"))
    if kwargs.pop("flush", False):
        file.flush()

stdin, stdout = IOWrapper(stdin), IOWrapper(stdout)
input = lambda: stdin.readline().rstrip("\r\n")

class FenwickTree:
    def __init__(self, a, n):
        self.a = a
        self.T = []
        for i in range(n):
            self.T.append(sum([self.a[j] for j in range(self.f(i), i + 1)]))
        
    def f(self, x):
        return x & (x + 1) 

    def get(self, i):
        res = 0
        while i >= 0:
            res += self.T[i]
            i = self.f(i) - 1
        return res

    def rsq(self, l, r):
        if l == 0:
            return self.get(r)
        return self.get(r) - self.get(l - 1)

    def set_(self, i, x):
        d = x - self.a[i]
        self.a[i] = x
        self.add(i, d)
    
    def add(self, i, x):
        j = i
        while j < n:
            self.T[j] += x
            j = j | (j + 1)
        
n = int(input())
a = list(map(int, input().split()))
tree = FenwickTree(a, n)

while True:
    oper = input().split()
    if oper:
        if oper[0] == 'sum':
            print(tree.rsq(int(oper[1]) - 1, int(oper[2]) - 1))
        else:
            tree.set_(int(oper[1]) - 1, int(oper[2]))
    else:
        break
