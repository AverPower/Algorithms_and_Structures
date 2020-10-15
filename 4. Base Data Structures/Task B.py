CAPACITY_CONST = 5
 
class Vector:
     
    def __init__(self, array = []):
        self.size = 0
        self.capacity = CAPACITY_CONST
        self.elements = [None] * self.capacity
        
    def get(self, i):
        if i < 0 or i > self.size:
            return Null
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
        
class Stack:
    
    def __init__(self):
        self.vector = Vector() 
    
    def push(self, data):
        self.vector.add(data)
        
    def pop(self):
        self.vector.erase()
        
    def size(self):
        return self.vector.size
    
    def back(self):
        return self.vector.elements[self.vector.size - 1]
    
    
polska_notation = input().split()
my_stack = Stack()
for symb in polska_notation:
    if symb.isdigit():
        my_stack.push(int(symb))
        
    else:
        a = my_stack.back()
        my_stack.pop()
        b = my_stack.back()
        my_stack.pop()
        if symb == '+':
            my_stack.push(a + b)
        elif symb == '-':
            my_stack.push(b - a)
        else:
            my_stack.push(a * b)
print(my_stack.back())
