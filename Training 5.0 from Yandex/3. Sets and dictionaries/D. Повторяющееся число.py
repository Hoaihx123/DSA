n, k = list(map(int, input().split()))
x = list(map(int, input().split()))
d = {}
for i in range(n):
    if x[i] in d:
        if i-d[x[i]] <= k:
            print('YES')
            exit()
    d[x[i]] = i
print('NO')
