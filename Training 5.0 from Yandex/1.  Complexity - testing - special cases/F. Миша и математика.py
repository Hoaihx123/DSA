n = int(input())
x = list(map(int, input().split()))
if x[0]%2:
    res = True
else:
    res = False
for i in range(n-1):
    if res:
        if x[i+1]%2:
            print('x', end='')
        else:
            print('+', end='')
    else:
        if x[i+1]%2:
            print('+', end='')
            res = True
        else:
            print('x', end='')