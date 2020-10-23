class Levenstein:
    
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end
        self.m = len(self.begin)
        self.n = len(self.end)
        d = [list(range(self.m + 1))]
        for i in range(self.n):
            d.append([i + 1] + [0] * self.m)
        self.d = d
    
    def distance(self):
        for i in range(1, self.n + 1):
            for j in range(1, self.m + 1):
                temp = []
                temp.append(self.d[i][j - 1] + 1) 
                temp.append(self.d[i - 1][j] + 1)
                if self.end[i - 1] == self.begin[j - 1]:
                    temp.append(self.d[i - 1][j - 1])
                else:
                    temp.append(self.d[i - 1][j - 1] + 1)
                self.d[i][j] = min(temp)
        return self.d[-1][-1]

begin = input()
end = input()

my_levenstein = Levenstein(begin, end)
print(my_levenstein.distance())
