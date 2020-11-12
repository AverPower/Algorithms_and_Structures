class Node:
    def __init__(self, key=None):
        self.key = key
        self.right = None
        self.left = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def search(self, v, x):
        if v == None:
            return None
        if v.key == x:
            return v
        elif x < v.key:
            return self.search(v.left, x)
        else:
            return self.search(v.right, x)
        
    def insert(self, v, x):
        if v == None:
            if self.root == None:
                self.root = Node(x)
            return Node(x)
        if x < v.key:
            v.left = self.insert(v.left, x)
        elif x > v.key:
            v.right = self.insert(v.right, x)
        return v
    
    def delete(self, v, x):
        if v == None:
            return None
        
        if x < v.key:
            v.left = self.delete(v.left, x)
        
        elif x > v.key:
            v.right = self.delete(v.right, x)
        
        elif v.left == None and v.right == None:
            if v == self.root:
                self.root = None
            v = None
        
        elif v.left == None:
            if v == self.root:
                self.root = v.right
            v = v.right
        
        elif v.right == None:
            if v == self.root:
                self.root = v.left
            v = v.left
        
        else:
            if v == self.root:
                self.root.key = self.findMax(v.left).key
                self.root.left = self.delete(v.left, x)
                v.key = self.root.key
                v.left = self.root.left
            else:
                v.key = self.findMax(v.left).key
                v.left = self.delete(v.left, x)
            
        return v
    
    def findMax(self, v):
        while v.right != None:
            v = v.right
        return v
    
    def printTree(self, v, indent=0):
        if v != None:
            self.printTree(v.left, indent + 2)
            print(indent * '_' + str(v.key))
            self.printTree(v.right, indent + 2)
        return
    
    
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
 
bst = BinarySearchTree()    

while True:
    try:
        line = input()
        if line:
            oper, i = line.split()
            i = int(i)
            if oper == 'insert':
                bst.insert(bst.root, i)
            elif oper == 'delete':
                bst.delete(bst.root, i)
            elif oper == 'exists':
                print('true' if bst.search(bst.root, i) else 'false')
            elif oper == 'next':
                print(bst.next(i))
            elif oper == 'prev':
                print(bst.prev(i))
    except:
        break

