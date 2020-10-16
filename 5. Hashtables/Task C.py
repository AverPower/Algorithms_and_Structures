from sys import stdout, stdin

A = 26
P = 31


class Node:
    
    def __init__(self, data = None):
        self.data = data
        self.prev = None
        self.next = None
    
    
class List: 

    def __init__(self):
        self.array = []
        
        
class LinkedHashMap:
    
    def __init__(self):
        self.p = P
        self.hashtable = [List() for i in range(self.p)] 
        self.header = None
        self.alpha = A 
        
    def put(self, k, v):
        
        cell = self.hashtable[self.h(k)].array
        for i, node in enumerate(cell):
            if node.data[0] == k:
                cell[i].data = (k, v)
                return
        newNode = Node((k, v))
        newNode.prev = self.header
        if self.header != None:
            self.header.next = newNode
        self.header = newNode
        cell.append(newNode)
  
    def delete(self, k): 
        
        cell = self.hashtable[self.h(k)].array
        for i, node in enumerate(cell):
            if node.data[0] == k:
                cell.remove(node)
                if node.prev == None and node.next == None:
                    self.header = None
                elif node.prev == None:
                    node.next.prev = None
                elif node.next == None:
                    node.prev.next = None
                    self.header = node.prev
                else:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                return
        
    def get(self, k):
        
        cell = self.hashtable[self.h(k)].array
        for i, node in enumerate(cell):
            if node.data[0] == k:
                return node.data[1]
        return 'none'
    
    def get_prev(self, k):
        
        cell = self.hashtable[self.h(k)].array
        for i, node in enumerate(cell):
            if node.data[0] == k:
                if node.prev != None:
                    return node.prev.data[1]
                else:
                    return 'none'
        return 'none'
    
    def get_next(self, k):
        
        cell = self.hashtable[self.h(k)].array
        for i, node in enumerate(cell):
            if node.data[0] == k:
                if node.next != None:
                    return node.next.data[1]
                else:
                    return 'none'
        return 'none'
    
    def h(self, x):
        result = 0 
        for i in range(len(x)):
            result = (result * self.alpha + ord(x[i])) % self.p
        return result


my_LinkedHashMap = LinkedHashMap()
args = stdin.readlines()
result = []
for line in args:
    oper = line.split()
    if oper[0] == 'put':
        my_LinkedHashMap.put( oper[1], oper[2])
    elif oper[0] == 'get':
        result.append(str(my_LinkedHashMap.get(oper[1])) + '\n')
    elif oper[0] == 'delete':
        my_LinkedHashMap.delete(oper[1])
    elif oper[0] == 'prev':
        result.append(str(my_LinkedHashMap.get_prev(oper[1])) + '\n')
    else:
        result.append(str(my_LinkedHashMap.get_next(oper[1])) + '\n')
stdout.writelines(result)
