a = [5, -8, 0, 9, 10, -3, 6, 2]
n = len(a)
for i in range(n-1):
    m = a[i]
    p = i
    for j in range(i, n, 1):
        if a[j] < m:
            m = a[j]
            p = j
    if p != i:
        a[p] = a[i]
        a[i] = m
print(a)