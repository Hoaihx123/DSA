n = int(input())
res = 0
for _ in range(n):
    x = int(input())
    res += x//4
    if x%4 == 3:
        res += 2
    else:
        res += x%4
print(res)