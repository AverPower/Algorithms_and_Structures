class Task_D:
    
    ALPH_LEN = 26
    
    def __init__(self):
        
        n, m = list(map(int, input().split()))
        self.n = n
        
        self.grisha_str = list(map(lambda x: ord(x) - ord('a'), input()))
                
        children_cards = input()

        ch_cnt = [0] * Task_D.ALPH_LEN
        for i in children_cards:
            ch_cnt[ord(i) - ord('a')] += 1
            
        self.ch_cnt = ch_cnt
        
    def checker(self, temp_cnt, add, delete = 0):
        
            if add != -1:
                if temp_cnt[self.grisha_str[add]] + 1 > self.ch_cnt[self.grisha_str[add]]:
                    return False
                else:
                    temp_cnt[self.grisha_str[add]] += 1
                    return True
            else:
                temp_cnt[self.grisha_str[delete]] -= 1
                return False
        
        
    def process(self):
              
        counter = 0 
        j = 0
        i = 0
        temp_cnt = [0] * Task_D.ALPH_LEN
        
        
        while True:
            while j < self.n and self.checker(temp_cnt, add = j):
                counter += j - i + 1
                j += 1

            else: 
                if i < self.n:
                    if self.checker(temp_cnt, add = -1, delete = i):
                        break
                    else:
                        i += 1
                else:
                    break
        return counter
                
        
task_d_solver = Task_D()

print(task_d_solver.process())
