n = int(input())
max_ = 0
res = set()
sum_ = 0
for i in range(1, n+1):
    a, b = list(map(int, input().split()))
    if a > b:
        sum_ += a-b
        res.add(i)
        if max_ < b:
            max_ = b
            index = i
    else:
        if max_ < a:
            index = i
            max_ = a
print(sum_+max_)

if index not in res:
    print(' '.join(str(s) for s in res), index, end=' ')
else:
    res.remove(index)
    print(' '.join(str(s) for s in res), index, end=' ')
for i in range(1, n+1):
    if i != index and i not in res:
        print(i, end=' ')


