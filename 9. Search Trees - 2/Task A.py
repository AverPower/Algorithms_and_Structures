from random import randint

RAND_UP = 10**5

class Node:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


def rand():
    return randint(1, RAND_UP)
        
class Treap:
    
    def __init__(self):
        self.root = None
    
    def split(self, v, x):
        if v == None:
            return (None,None)
        if x < v.key:
            t1, t2 = self.split(v.left, x)
            v.left = t2
            return t1, v
        t1, t2 = self.split(v.right, x)
        v.right = t1
        return v, t2
    
    def merge(self, t1, t2):
        if t1 == None:
            return t2
        if t2 == None:
            return t1
        if t1.value > t2.value:
            t1.right = self.merge(t1.right, t2)
            return t1
        t2.left = self.merge(t1, t2.left)
        return t2
    
    def find(self, v, x):
        if v == None:
            return 'false'
        if v.key == x:
            return 'true'
        if v.key > x:
            return self.find(v.left, x)
        return self.find(v.right, x)
    
    def insert(self, x):
        node = Node(x, rand())
        if self.root == None:
            self.root = node
            return
        t1, t2 = self.split(self.root, x)
        t1 = self.merge(t1, node)
        self.root = self.merge(t1, t2)
        
    def remove(self, x):
        t1, t2 = self.split(self.root, x)
        t11, t12 = self.split(t1, x - 1)
        self.root = self.merge(t11, t2)

    def next(self, x):
        v = self.root
        res = None
        while v != None:
            if v.key > x:
                res = v
                v = v.left
            else:
                v = v.right
        if res:
            return res.key
        else:
            return 'none'
    
    def prev(self, x):
        v = self.root
        res = None
        while v != None:
            if v.key < x:
                res = v
                v = v.right
            else:
                v = v.left
                    
        if res:
            return res.key
        else:
            return 'none'
        
    def search(self, x):
        return self.find(self.root, x)
        
    def printTree(self, v, indent=0):
        if v != None:
            self.printTree(v.left, indent + 2)
            print(indent * '_' + str(v.key) + '_' + str(v.value))
            self.printTree(v.right, indent + 2)
        return
    
    def print(self):
        self.printTree(self.root)
            
treap = Treap()    

while True:
    try:
        line = input()
        if line:
            oper, i = line.split()
            i = int(i)
            if oper == 'insert':
                treap.insert(i)
            elif oper == 'delete':
                treap.remove(i)
            elif oper == 'exists':
                print(treap.search(i))
            elif oper == 'next':
                print(treap.next(i))
            elif oper == 'prev':
                print(treap.prev(i))
    except:
        break
