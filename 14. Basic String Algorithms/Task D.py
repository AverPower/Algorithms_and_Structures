from sys import stdin, stdout

WORD_MAX_LEN = 30
VERTEX_MAX_COUNT = 10 ** 5

class Vertex:
    def __init__(self, alphabet):
        self.next = dict()
        for c in alphabet:
            self.next[c] = -1
        self.isTerminal = False
        
class Trie:
    def __init__(self, alphabet):
        self.size = 1
        self.alphabet = alphabet
        self.t = [0] * VERTEX_MAX_COUNT
        self.t[0] = Vertex(alphabet)

    def insert(self, s):
        v = 0
        for i in range(len(s)):
            if self.t[v].next[s[i]] == -1:
                self.t[v].next[s[i]] = self.size
                self.size += 1
                self.t[self.t[v].next[s[i]]] = Vertex(alphabet)
            v = self.t[v].next[s[i]]
        self.t[v].isTerminal = True
        
    def contains(self, s):
        v = 0
        res = []
        for i in range(len(s)):
            if self.t[v].next[s[i]] == -1:
                return res
            v = self.t[v].next[s[i]]
            if self.t[v].isTerminal == True:
                res.append(i)
        return res
        
start = ord('a')
alphabet = [chr(i) for i in range(start, start + 26)]
trie = Trie(alphabet)
args = stdin.read().split("\n")
find_str = args[0]
m = int(args[1])
for word in args[2:-1]:
    trie.insert(word)
    
words_dict = dict.fromkeys(args[2:-1], 0)

for i in range(len(find_str)):
    end = trie.contains(find_str[i: i + WORD_MAX_LEN])
    for j in end:
        words_dict[find_str[i:i + j + 1]] = 1

res = []        
for word in args[2:-1]:
    if words_dict[word]:
        res.append("Yes")
    else:
        res.append("No")
stdout.write("\n".join(res))
