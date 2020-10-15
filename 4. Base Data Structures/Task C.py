from sys import stdin, stdout
 
CAPACITY_CONST = 4
 
class Vector:
    
    def __init__(self):
        self.begin = 0
        self.end = 0
        self.capacity = CAPACITY_CONST
        self.elements = [None] * self.capacity
           
    def add(self, data):
        if (self.end + 1)% self.capacity == self.begin:
            self.changeCapacity(1)
        self.elements[self.end] = data
        self.end =  (self.end + 1) % self.capacity
        
    def changeCapacity(self, encrease):
        new_end = self.get_size() 
        old_capacity = self.capacity
        
        self.capacity = self.capacity * 2 if encrease else self.capacity // 4
        new_elements = self.capacity * [None]
        i = self.begin
        while i != self.end % old_capacity:
            new_elements[i % old_capacity] = self.elements[i % old_capacity]
            i = (i + 1) % old_capacity
        
        self.elements = new_elements
        self.begin = 0
        self.end = new_end
        
    def erase(self):
        erased = self.elements[self.begin]
        if self.get_size() < self.capacity // 4:
            self.changeCapacity(0)
        self.begin = (self.begin + 1) % self.capacity
        return erased
        
    def get_size(self):
        return self.end - self.begin if self.end > self.begin else self.capacity - self.begin + self.end 
        
        
class Queue:
    
    def __init__(self):
        self.vector = Vector() 
    
    def push(self, data):
        self.vector.add(data)
        
    def pop(self):
        return self.vector.erase()
        
    def size(self):
        return self.vector.get_size()
    
    def front(self):
        return self.vector.elements[begin]
    
    
operation_num = int(input())
my_queue = Queue()
result = []
 
for i in range(operation_num):
    line = input().split()
    if len(line) == 2:
        my_queue.push(int(line[1]))
    else:
        result.append(my_queue.pop())
for r in result:
    print(r)
