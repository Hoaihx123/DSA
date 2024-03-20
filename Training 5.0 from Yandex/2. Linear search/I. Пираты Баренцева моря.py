n = int(input())
x = [list(map(int, input().split())) for _ in range(n)]
x.sort(key=lambda c: c[0])
res = 0
for i in range(1, n+1):
    res += abs(x[i-1][0]-i)
m = 100000000
for i in range(n):
    tem = i
    m = min(m, sum(abs(a[1]-i-1) for a in x))
res += m
print(res)