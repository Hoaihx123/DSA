n = int(input())
input()
res = set(input().split())
for _ in range(n-1):
    input()
    s = set(input().split())
    res = res.intersection(s)
print(len(res))
print(' '.join(sorted(res)))
