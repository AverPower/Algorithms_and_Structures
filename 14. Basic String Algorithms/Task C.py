def pfunction(s):
    n = len(s)
    p = [0] * n
    for i in range(1, n):
        k = p[i - 1]
        while k > 0 and s[i] != s[k]:
            k = p[k - 1]
        if s[i] == s[k]:
            k += 1
        p[i] = k
    return p
    
    
p = input()
t = input()
pref = pfunction(p + "#" + t)

res = []
n = len(p)
for i in range(len(pref)):
    if pref[i] == n:
        res.append(i)
print(len(res))
print(*[i - 2 * n + 1 for i in res])
