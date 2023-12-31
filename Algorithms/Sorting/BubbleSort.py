a = [5, -8, 0, 9, 10, -3, 6, 2]
n = len(a)
for i in range(n-1, 0, -1):
    for j in range(i):
        if a[j+1] < a[j]:
            a[j+1], a[j] = a[j], a[j+1]
print(a)

