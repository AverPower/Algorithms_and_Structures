from sys import stdin, stdout

P = 31
A = 26

class Array:
    def __init__(self):
        self.a = []

class Map:
    
    def __init__(self):
        self.p = P
        self.hashtable = [Array() for i in range(self.p)] 
        self.alpha = A 
        
    def insert(self, k, v):
        array = self.hashtable[self.h(k)].a
        for i, cell in enumerate(array):
            if cell[0] == k:
                array[i] = (k, v)
                return
        array.append((k,v)) 
        
    def delete(self, k): 
        array = self.hashtable[self.h(k)].a
        for i, cell in enumerate(array):
            if cell[0] == k:
                array.remove(array[i])
                return
        
    def get(self, k):
        array = self.hashtable[self.h(k)].a
        for cell in array:
            if cell[0] == k:
                return cell[1]
        return None 
  
    def h(self, x):
        result = 0 
        for i in range(len(x)):
            result = (result * self.alpha + ord(x[i])) % self.p
        return result

my_map = Map()
args = stdin.readlines()
result = []

for operation in args:

    line = operation.split()
    if line[0] == 'put':
          my_map.insert(line[1], line[2])
    elif line[0] == 'delete':
          my_map.delete(line[1])
    else:
        h = my_map.get(line[1])
        result.append(h + '\n' if h != None else 'none\n')

stdout.writelines(result)
