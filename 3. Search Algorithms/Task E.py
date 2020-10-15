def lower_bound(left, right, f, speed_copy_1, speed_copy_2):
    if left == right - 1:
        return right + min(speed_copy_1, speed_copy_2)
    middle = (left + right) // 2
    if f(middle, speed_copy_1, speed_copy_2, n):
        return lower_bound(middle, right, f, speed_copy_1, speed_copy_2)
    else:
        return lower_bound(left, middle, f, speed_copy_1, speed_copy_2)
    

def f(time, speed_copy_1, speed_copy_2, n):
    return time // speed_copy_1 + time // speed_copy_2 < n - 1 
 
n, speed_copy_1, speed_copy_2 = map(int, input().split())

print(lower_bound(-1, (n-1) * max(speed_copy_1, speed_copy_2) + 1, f, speed_copy_1, speed_copy_2))
