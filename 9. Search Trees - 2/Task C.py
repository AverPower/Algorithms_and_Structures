from random import randint

RAND_UP = 10**6

class Node:
    
    def __init__(self, value, priority):
        self.priority = priority
        self.value = value
        self.size = 1
        self.left = None
        self.right = None

    
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
    
    def insert(self, x, pos):
        node = Node(x, rand())
        if self.root == None:
            self.root = node
            return
        t1, t2 = self.split(self.root, pos)
        t1 = self.merge(t1, node)
        self.root = self.merge(t1, t2)    
        
    def move(self, l, r):
        t1, t2 = self.split(self.root, l)
        t21, t22 = self.split(t2, r - l)
        t = self.merge(t21, t1)
        self.root = self.merge(t, t22)
        
    def printTree(self, v):
        if v != None:
            self.printTree(v.left)
            print(str(v.value), end=' ')
            self.printTree(v.right)
        return
    
    def print(self):
        self.printTree(self.root)
    
treap = TreapImplicitKey()
n, m = map(int, input().split())
for i in range(n):
    treap.insert(i + 1, i)

for _ in range(m):
    params = list(map(lambda x: int(x) - 2, input().split()))
    treap.move(params[0], params[1])
treap.print()
