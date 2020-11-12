from random import randint
from sys import stdout, stdin
from io import IOBase, BytesIO
from os import read, write, fstat
 
BUFSIZE = 8192
 
RAND_UP = 10**6
 
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
    
        
class Node:
    
    def __init__(self, value, priority):
        self.priority = priority
        self.value = value
        self.size = 1
        self.left = None
        self.right = None
        self.is_reverse = False
        

def rand():
    return randint(1, RAND_UP)
        
class TreapImplicitKey:
    
    def __init__(self):
        self.root = None
       
    def get_size(self, v):
        return v.size if v != None else 0
    
    def fix(self, v):
        v.size = self.get_size(v.left) + self.get_size(v.right) + 1
    
    def split(self, v, x):
        self.push(v)
        if v == None:
            return (None,None)
        if self.get_size(v.left) > x:
            t1, t2 = self.split(v.left, x)
            v.left = t2
            self.fix(v)
            return t1, v
        t1, t2 = self.split(v.right, x - self.get_size(v.left) - 1)
        v.right = t1
        self.fix(v)
        return v, t2
    
    def merge(self, t1, t2):
        self.push(t1)
        self.push(t2)
        if t1 == None:
            return t2
        if t2 == None:
            return t1
        if t1.priority > t2.priority:
            t1.right = self.merge(t1.right, t2)
            self.fix(t1)
            return t1
        t2.left = self.merge(t1, t2.left)
        self.fix(t2)
        return t2
    
    def from_vector(self, array):
        result = None
        for a in array:    
            result = self.merge(result, Node(a, rand()))
        self.root = result
        
    def swap(self, v):
        v.right, v.left = v.left, v.right
        if v.right != None:
            v.right.is_reverse ^= True
        if v.left != None:
            v.left.is_reverse ^= True
        
    def reverse(self, l, r):
        t1, t2 = self.split(self.root, l)
        t21, t22 = self.split(t2, r - l)
        self.swap(t21)
        t = self.merge(t1, t21)
        self.root = self.merge(t, t22)
    
    def push(self, v):
        if v == None or v.is_reverse == False:
            return
        self.swap(v)
        v.is_reverse = False
        
    def printTree(self, v):
        if v != None:
            self.push(v)
            self.printTree(v.left)
            print(str(v.value), end=' ')
            self.printTree(v.right)
        return
    
    def print(self):
        self.printTree(self.root)
        
stdin, stdout = IOWrapper(stdin), IOWrapper(stdout)
input = lambda: stdin.readline().rstrip("\r\n")
    
treap = TreapImplicitKey()
n, m = map(int, input().split())
treap.from_vector(range(1, n + 1))

for _ in range(m):
    params = list(map(lambda x: int(x) - 2, input().split()))
    treap.reverse(params[0], params[1])
treap.print()
