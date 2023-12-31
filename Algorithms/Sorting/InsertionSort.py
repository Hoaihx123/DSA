a = [5, -8, 0, 9, 10, -3, 6, 2]
n = len(a)
for i in range(1, n):
    for j in range(i, 0, -1):
        if a[j] < a[j-1]:
            a[j], a[j-1] = a[j-1], a[j]
        else:
            break
print(a)