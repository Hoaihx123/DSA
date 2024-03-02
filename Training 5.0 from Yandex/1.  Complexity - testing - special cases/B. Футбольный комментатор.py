a, b = map(int, input().split(':'))
c, d = map(int, input().split(':'))
x = int(input())
if (a+c > b+d):
    print(0)
else:
    res = b+d-a-c+1
    if (a>d and x==2) or  (a<d and x==1):
        res -= 1
    print(res)