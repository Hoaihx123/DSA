x = []
for _ in range(3):
    input()
    x.append(set(map(int, input().split())))
s = set()
s.update(x[1])
s.update(x[0])
s.update(x[2])
for key in s:
    count = 0
    if key in x[0]:
        count += 1
    if key in x[1]:
        count += 1
    if key in x[2]:
        count += 1
    if count >= 2:
        print(key, end=' ')