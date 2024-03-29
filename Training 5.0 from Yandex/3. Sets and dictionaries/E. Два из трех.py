x = {}
for _ in range(3):
    input()
    s = set(map(int, input().split()))
    for a in s:
        if a in x:
            x[a] += 1
        else:
            x[a] = 1
res = []
for key in x:
    if x[key] > 1:
        res.append(key)
res.sort()
print(*res)