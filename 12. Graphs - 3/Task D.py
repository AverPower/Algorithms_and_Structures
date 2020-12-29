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
    """Prints the values to a stream, or to sys.stdout by default."""
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

class Crascall:
    def __init__(self, n, edges, weights):
        self.n = n
        self.p = list(range(self.n))
        self.r = [0] * self.n
        self.edges = edges
        self.weights = weights
        
    def get_p(self, x):
        if self.p[x] != x:
            self.p[x] = self.get_p(self.p[x])
        return self.p[x]
    
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
        
    def span(self):
        result = 0
        for (u, v) in self.edges:
            if self.get_p(u) != self.get_p(v):
                result += self.weights[(u, v)]
                self.join(u, v)
        return result

stdin, stdout = IOWrapper(stdin), IOWrapper(stdout)
input = lambda: stdin.readline().rstrip("\r\n")

args = stdin.readlines()
weights = dict()
n, m = map(int, args[0].split())
for line in args[1:]:
    b, e, w = map(int, line.split())
    b -= 1
    e -= 1
    if weights.get((b, e), 0):
        weights[(b, e)] = min(weights[(b, e)], w)
    else:
        weights[(b, e)] = w
        
edges = [i[0] for i in sorted(weights.items(), key=lambda x: x[1])]
crascall = Crascall(n, edges, weights)
print(crascall.span())
