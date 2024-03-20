n = int(input())
x = list(map(int, input().split()))
a, b, k = list(map(int, input().split()))
a = max((a-1)//k, 0)
b = max((b-1)//k, 0)
if b-a>=n:
    print(max(x))
    exit()
if a%n <= b%n:
    max_=max(x[a%n:b%n+1])
    for i in range(-(b%n), -(a%n)+1):
        if max_<x[i]:
            max_=x[i]
    print(max_)
else:
    print(a % n, b % n)
    max_ = max(max(x[a%n:n]), max(x[0:b%n+1]))
    for i in range(-n, -(a % n)+1):
        if max_ < x[i]:
            max_ = x[i]
    for i in range(-(b % n), 0):
        if max_ < x[i]:
            max_ = x[i]
    print(max_)
