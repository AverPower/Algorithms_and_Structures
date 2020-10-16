from math import inf
from sys import stdout, stdin



P_BIG = 9369319
A_BIG = 451543
P_SMALL = 31
A_SMALL = 26

        
class MultiMap:
    
    def __init__(self):
        self.hash_p = P_BIG
        self.a = [None] * self.hash_p
        self.size = 0
        self.hash_a = A_BIG
        self.ripcnt = 0
        
    def insert(self, x, y):
        
        if self.size + self.ripcnt >= self.hash_p / 2:
            self.doRehashing()
                    
        i = self.h(x)
        while self.a[i] != None:
            if self.a[i] == inf:
                self.ripcnt -= 1
                break
            if self.a[i].x == x:
                self.a[i].insert(y)
                return
            i = (i + 1) % self.hash_p
        
        self.a[i] = HashMap(x)
        self.a[i].insert(y)
        self.size += 1
        
    def get(self, x):
        i = self.h(x)
        while self.a[i] != None:
            if self.a[i] != inf:
                if self.a[i].x == x:
                    return self.a[i].get()
            i = (i + 1) % self.hash_p
        return '0\n'
        
    def doRehashing(self):
        self.hash_p =  self.n * 4
        a_new = self.a.copy()
        self.a = [None] * self.hash_p
        self.ripcnt = 0
        self.n = 0
        for x in a_new:
            if x != None and x != inf:
                self.insert(x)
        
        
    def delete(self, x, y):    
        i = self.h(x)
        while self.a[i] != None:
            if self.a[i] != inf:
                if self.a[i].x == x:
                    self.a[i].delete(y)
                    if self.a[i].num == 0:
                        self.a[i] = inf
                        self.ripcnt += 1
                    break
            i = (i + 1) % self.hash_p    
    
    def delete_all(self, x):
        i = self.h(x)
        while self.a[i] != None:
            if self.a[i] != inf:
                if self.a[i].x == x:
                    self.a[i] = inf
                    self.ripcnt += 1
            i = (i + 1) % self.hash_p
    
    def h(self, x):
        result = 0 
        for i in range(len(x)):
            result = (result * self.hash_a + ord(x[i])) % self.hash_p
        return result
    
    
class Array:
    def __init__(self):
        self.a = []

class HashMap:
    
    def __init__(self, x):
        
        self.p = P_SMALL
        self.hashtable = [Array() for i in range(self.p)] 
        self.alpha = A_SMALL 
        self.x = x
        self.num = 0
        
    def insert(self, y):
        array = self.hashtable[self.h_jun(y)].a
        if y in array:
            return
        array.append(y)
        self.num += 1
        
    def delete(self, y): 
        array = self.hashtable[self.h_jun(y)].a
        if y in array:
            array.remove(y)
            self.num -= 1
            
    def get(self):
        n_pairs = 0
        y_all = []
        for i in range(self.p):
            for y in self.hashtable[i].a:
                y_all.append(y)
                n_pairs += 1
        return f'{str(n_pairs)} {" ".join(y_all)}\n'
        
    
    def h_jun(self, x):
        result = 0 
        for i in range(len(x)):
            result = (result * self.alpha + ord(x[i])) % self.p
        return result
        
my_MP = MultiMap()

args = stdin.readlines()
result = []

for oper in args:
    line = oper.strip().split(' ')
    if line[0] == 'put':
        my_MP.insert(line[1], line[2])
    elif line[0] == 'get':
        result.append(my_MP.get(line[1]))
    elif line[0] == 'delete':
        my_MP.delete(line[1], line[2])
    else:
        my_MP.delete_all(line[1])
stdout.writelines(result)
