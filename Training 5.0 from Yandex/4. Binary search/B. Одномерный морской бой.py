n = int(input())
def check(k, n):
    return k*(k+1)*(k+5)//6-1 <= n
l, r = 0, n
while l < r:
    m = (l+r+1)//2
    if check(m, n):
        l = m
    else:
        r = m-1
print(l)
