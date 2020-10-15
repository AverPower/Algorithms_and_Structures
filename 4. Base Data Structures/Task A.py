from sys import stdout, stdin
from io import IOBase, BytesIO
from os import read, write, fstat

BUFSIZE = 8192

class Node:

    def __init__ (self, data = None):
        self.data = data
        self.next = None
        

class LinkedList: 

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def print_list(self):
        cur_node = self.head
        while (cur_node != None):
            print(cur_node.data)
            cur_node = cur_node.next

    def insert(self, data):
        new_node = Node(data)

        if self.size == 0:
            self.head = new_node
        else:
            self.tail.next = new_node

        self.tail = new_node
        self.size += 1

    def insert_from_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def erase(self, i):
        if i == 0:
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
        else:
            prev = self.head 
            cur = prev.next
            j = 1
            
            while j < i:
                prev = cur
                cur = prev.next
                j += 1
            
            prev.next = cur.next
            if cur == self.tail:
                self.tail = prev
        self.size -= 1

class Stack():

    def __init__(self):
        self.list = LinkedList()
        self.min_list = LinkedList()

    def pop(self):
        self.list.erase(0)
        self.min_list.erase(0)

    def add(self, data):
        if self.size() == 0:
            self.min_list.insert_from_begin(data)
        else:
            cur_min = self.min_list.head.data
            self.min_list.insert_from_begin(min(cur_min, data))
        self.list.insert_from_begin(data)

    def size(self):
        return self.list.size

    def back(self):
        return self.list.head.data

    def get_minim(self):
        return self.min_list.head.data


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

stdin, stdout = IOWrapper(stdin), IOWrapper(stdout)
args = stdin.readlines()
operation_num = int(args[0])
my_stack = Stack()
result = []

for i in range(operation_num):
    line = list(map(int, args[i + 1].split()))
    if line[0] == 1:
        my_stack.add(line[1])
    elif line[0] == 2:
        my_stack.pop()
    else:
        result.append(str(my_stack.get_minim()) + '\n')
stdout.writelines(result)
