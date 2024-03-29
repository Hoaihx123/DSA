n = int(input())
arr = list(map(int, input().split()))
arr.sort()
k = int(input())
for _ in range(k):
    L, R = list(map(int, input().split()))
    start, end = 0, n
    while start < end:
        med_1 = (start + end) // 2
        if arr[med_1] >= L:
            end = med_1
        else:
            start = med_1+1
    med_1 = start
    start, end = 0, n
    while start < end:
        med_2 = (start + end) // 2
        if arr[med_2] > R:
            end = med_2
        else:
            start = med_2+1
    med_2 = start
    print(med_2-med_1, end=' ')
