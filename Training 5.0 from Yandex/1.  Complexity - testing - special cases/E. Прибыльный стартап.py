n, k, d = list(map(int, input().split()))

if n*10%k == 0:
    n = n*10
else:
    x = (n*10//k+1)*k
    if x < (n+1)*10:
        n = x
    else:
        print(-1)
        exit()
print(str(n)+'0'*(d-1))
