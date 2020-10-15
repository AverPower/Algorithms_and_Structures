from sys import stdin, stdout
from math import inf
CAPACITY_CONST = 4
 
class Vector:
     
    def __init__(self):
        self.size = 0
        self.capacity = CAPACITY_CONST
        self.elements = [None] * self.capacity
        
    def get(self, i):
        if i < 0 or i > self.size:
            return None
        return self.elements[i]
    
    def add(self, data):
        if self.size + 1 > self.capacity:
            self.changeCapacity(1)
        
        self.elements[self.size] = data
        self.size += 1
        
    def changeCapacity(self, encrease):
        self.capacity = self.capacity * 2 if encrease else self.capacity // 4
        new_elements = self.capacity * [None]
        for i in range(self.size):
            new_elements[i] = self.elements[i]
        self.elements = new_elements
        
    def erase(self):
        if self.size - 1 < self.capacity // 4:
            self.changeCapacity(0)
        self.size -= 1
        
        
class Heap:
    
    def __init__(self):
        self.vector = Vector()
        self.elements = self.vector.elements
        self.operation_counter = 0
        
    def insert(self, x):
        self.operation_counter += 1
        i = self.vector.size
        self.vector.add((x, self.operation_counter))
 
        while i > 0:
            if self.vector.elements[i] < self.vector.elements[(i - 1) // 2]:
                self.swap(i, (i - 1) // 2)
            else:
                break
            i = (i - 1) // 2
            
    def removeMin(self):
        
        self.operation_counter += 1
        if self.vector.size == 0:
            return '*\n'
        res, oper = self.vector.elements[0]
 
        self.swap(0, self.vector.size - 1)
        self.vector.erase()
        i = 0
        while 2 * i + 1 < self.vector.size:
            cur = self.vector.elements[i]
            left = self.vector.elements[2 * i + 1]
            if 2 * i + 2 == self.vector.size:
                right = (inf, inf)
            else:
                right = self.vector.elements[2 * i + 2]
            if left < right and left < cur:
                self.swap(i, 2 * i + 1)
                i = 2 * i + 1
            elif right < cur and right < left:
                self.swap(i, 2 * i + 2)
                i = 2 * i + 2
            else:
                break            
        return str(res) + ' ' + str(oper) + '\n'
            
    def decrease_key(self, oper_num, decr_value):
        
        self.operation_counter += 1
        
        for idx in range(self.vector.size):
            if self.vector.get(idx)[1] == oper_num:
                break
        else:
            return 
        
        self.vector.elements[idx] = (decr_value, oper_num)
             
        while idx > 0:
            if self.vector.elements[idx] < self.vector.elements[(idx - 1) // 2]:
                self.swap(idx, (idx - 1) // 2)
            else:
                break
            idx = (idx - 1) // 2
    
    def swap(self, i, j):
        self.vector.elements[i], self.vector.elements[j] = self.vector.elements[j], self.vector.elements[i]      
        
my_heap = Heap()
args = stdin.readlines()
result = []
 
for operation in args:
    
    line = operation.split()
    if line[0] == 'push':
        my_heap.insert(int(line[1]))
    elif line[0] == 'extract-min':
        result.append(my_heap.removeMin())
    else:
        my_heap.decrease_key(int(line[1]), int(line[2]))
        
stdout.writelines(result)
