n, m = list(map(int, input().split()))
a = [input() for _ in range(n)]
count = [[0 for _ in range(m+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        t = 1 if a[i-1][j-1] == '#' else 0
        count[i][j] = count[i-1][j]+count[i][j-1]-count[i-1][j-1]+t
def acreage(x2, y2, x1, y1):
    return count[x2+1][y2+1]-count[x1][y2+1]-count[x2+1][y1]+count[x1][y1]
def check(k):
    for i in range(n-3*k+1):
        for j in range(m-3*k+1):
            if acreage(i+3*k-1, j+2*k-1, i, j+k) != 3*k*k:
                continue
            if acreage(i+2*k-1, j+k-1, i+k, j) != k*k:
                continue
            if acreage(i+2*k-1, j+3*k-1, i+k, j+2*k) == k*k:
                return True
    return False

left, right = 0, min(n, m)
while left < right:
    mid = (left+right+1)//2
    if check(mid):
        left = mid
    else:
        right = mid-1
print(left)
