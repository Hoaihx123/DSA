horizontal = set()
vertical = set()
n = int(input())
res = 0
for _ in range(n):
    x, y = list(map(int, input().split()))
    if (x, y) not in horizontal:
        horizontal.add((x, y))
        res += 1
    else:
        res -=1
    if (x, y+1) not in horizontal:
        horizontal.add((x, y+1))
        res += 1
    else:
        res -=1
    if (x, y) not in vertical:
        vertical.add((x, y))
        res += 1
    else:
        res -=1
    if (x+1, y) not in vertical:
        vertical.add((x+1, y))
        res += 1
    else:
        res -=1

print(res)

