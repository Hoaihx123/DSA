n = int(input())
x = list(map(int, input().split()))
d = {}
for a in x:
    if a in d:
        d[a] += 1
    else:
        d[a] = 1
res = 0
for key in d:
    max_ = d[key]
    if key-1 in d:
        max_ = d[key]+d[key-1]
    if key+1 in d:
        max_ = max(max_, d[key]+d[key+1])
    res = max(max_, res)
print(n-res)

