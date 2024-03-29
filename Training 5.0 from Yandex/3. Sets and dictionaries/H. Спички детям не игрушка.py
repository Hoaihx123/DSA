n = int(input())
img_1 = {}
for _ in range(n):
    x1, y1, x2, y2 = list(map(int, input().split()))
    if x1 < x2 or (x1 == x2 and y1 < y2):
        x1, y1, x2, y2 = x2, y2, x1, y1

    if (x1 - x2, y1 - y2) in img_1:
        img_1[(x1 - x2, y1 - y2)].add((x2, y2))
    else:
        img_1[(x1 - x2, y1 - y2)] = {(x2, y2)}
res = {}
for _ in range(n):
    x1, y1, x2, y2 = list(map(int, input().split()))
    if x1 < x2 or (x1 == x2 and y1 < y2):
        x1, y1, x2, y2 = x2, y2, x1, y1
    if (x1-x2, y1-y2) in img_1:
        for p in img_1[(x1-x2, y1-y2)]:

            if (x2-p[0], y2-p[1]) in res:
                res[(x2-p[0], y2-p[1])] += 1
            else:
                res[(x2 - p[0], y2 - p[1])] = 1
max_v = 0
for x in res:
    if res[x] > max_v:
        max_v = res[x]
print(n-max_v)