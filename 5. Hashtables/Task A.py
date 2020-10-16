from math import inf
from random import randint
from sys import stdout, stdin
from io import IOBase, BytesIO
from os import read, write, fstat


M = 9121511
P = 9369319
A = 451543
 
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

class Map:
    
    def __init__(self):
        self.array = [None] * M
        self.size = 0
        self.m = M
        self.hash_p = P
        self.hash_a = A
        self.ripcnt = 0
        
    def insert(self, x):
        
        if self.size + self.ripcnt >= self.m :
            self.doRehashing()
                    
        i = self.h(x)
        while self.array[i] != None:
            if self.array[i] == inf:
                self.array[i] = x
                self.size += 1
                self.ripcnt -= 1
            if self.array[i] == x:
                return
            i = (i + 1) % self.m
        
        self.array[i] = x
        self.size += 1
        
    def exists(self, x):
        i = self.h(x)
        while self.array[i] != None:
            if self.array[i] == x:
                return i
            i = (i + 1) % self.m
        return None
        
    def doRehashing(self):
        self.m =  self.size * 4
        a_new = self.array.copy()
        self.array = [None] * self.m
        self.ripcnt = 0
        self.size = 0
        for x in a_new:
            if x != None and x != inf:
                self.insert(x)    
        
    def delete(self, x):    
        i = self.h(x)
        while self.array[i] != None:
            if self.array[i] == x:
                self.array[i] = inf
                self.ripcnt += 1
                break
            i = (i + 1) % self.m    
        
    
    def h(self, x):
        return (self.hash_a * x) % (self.hash_p) % self.m

stdin, stdout = IOWrapper(stdin), IOWrapper(stdout)
input = lambda: stdin.readline().rstrip("\r\n")
my_map = Map()
result = []
 
while True:
    operation = input()
    if operation:
        line = operation.split()
        if line[0] == 'insert':
            my_map.insert(int(line[1]))
        elif line[0] == 'delete':
            my_map.delete(int(line[1]))
        else:
            print('true' if my_map.exists(int(line[1])) != None else 'false')
    else:
        break
        
stdout.writelines(result)
