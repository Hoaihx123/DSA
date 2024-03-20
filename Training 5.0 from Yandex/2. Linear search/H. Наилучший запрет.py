n, m = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(n)]
def find_max(a, row, col):
    res = -1000000
    row_, col_ = -1, -1
    for i in range(n):
        if i == row:
            continue
        for j in range(m):
            if j == col:
                continue
            if a[i][j] > res:
                res = a[i][j]
                row_, col_ = i, j
    return [res, row_, col_]
max_1 = find_max(a, -1, -1)
max_2 = find_max(a, max_1[1], -1)
count_max_2 = find_max(a, max_1[1], max_2[2])
max_3 = find_max(a, -1, max_1[2])
count_max_3 = find_max(a, max_3[1], max_1[2])
if count_max_2[0] < count_max_3[0]:
    print(max_1[1]+1, max_2[2]+1)
else:
    print(max_3[1]+1, max_1[2]+1)