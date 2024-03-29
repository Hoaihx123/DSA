n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
for i in range(1, n):
    a[i] += a[i-1]
def check(k, l):
    if k+l > n:
        return float('inf')
    if k == 0:
        return a[l-1]
    return a[k+l-1]-a[k-1]
for _ in range(m):
    l, s = list(map(int, input().split()))
    left, right = 0, n
    while left < right:
        m = (left+right)//2
        if check(m, l) >= s:
            right = m
        else:
            left = m+1
    if check(left, l) == s:
        print(left+1)
    else:
        print(-1)
