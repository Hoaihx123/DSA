n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
res = 0
for i in range(max(n-k, 1)):
    min_ = arr[i]
    for j in range(i, min(i+k+1, n)):
        if arr[j] < min_:
            min_ = arr[j]
        elif arr[j] > min_:
            res = max(arr[j]-min_, res)
print(res)