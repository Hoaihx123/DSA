n = int(input())
s = set()

for _ in range(n):
    s.add(tuple(map(int, input().split())))
if n == 1:
    for x in s:
        print(3)
        print(x[0]+1, x[1])
        print(x[0]+1, x[1]+1)
        print(x[0], x[1])
        exit()
res = []
for i in s:
    temp_1 = []
    for j in s:
        if j == i:
            continue
        temp_2 = [i, j]
        a, b = j[0]-i[0], j[1] - i[1]
        a, b = -b, a
        x = (j[0]+a, j[1]+b)
        if x in s:
            temp_2.append(x)
            a, b = -b, a
            x = (x[0]+a, x[1]+b)
            if x in s:
                temp_2.append(x)
        if len(temp_2) > len(temp_1):
            temp_1 = temp_2.copy()
    if len(temp_1) > len(res):
        res = temp_1.copy()
    if len(temp_1) == 4:
        print(0)
        exit()
a, b = res[1][0]-res[0][0], res[1][1]-res[0][1]
print(4-len(res))
if len(res) == 2:
    print(res[1][0]-b, res[1][1]+a)
    print(res[1][0]-b-a, res[1][1]+a-b)
else:
    print(res[2][0]-a, res[2][1]-b)





