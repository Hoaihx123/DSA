k = int(input())
x_max, y_max, x_min, y_min = -1000000, -1000000, 1000000, 1000000
for _ in range(k):
    x, y = list(map(int, input().split()))
    x_max = max(x_max, x)
    x_min = min(x_min, x)
    y_max = max(y_max, y)
    y_min = min(y_min, y)
print(x_min, y_min, x_max, y_max)