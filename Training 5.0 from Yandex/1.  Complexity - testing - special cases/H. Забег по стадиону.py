l, x1, v1, x2, v2 = list(map(int, input().split()))
res = 1000000
if v1-v2>0:
    k = (x1-x2)//l
    if (x1-x2)%l:
        k+=1
    res = float((k*l-x1+x2)/(v1-v2))
elif v1-v2<0:
    k = (x1-x2)//l
    res = float((k * l - x1 + x2) / (v1 - v2))
else:
    if x1==x2:
        print('YES')
        print(0)
        exit()
if v1+v2>0:
    k = (x1+x2)//l
    if (x1+x2)%l:
        k+=1
    res = float((k*l-x1-x2)/(v1+v2)) if float((k*l-x1-x2)/(v1+v2)) < res else res
elif v1+v2<0:
    k = (x1 + x2) // l
    res = float((k * l - x1 - x2) / (v1 + v2)) if float((k * l - x1 - x2) / (v1 + v2)) < res else res
else:
    if (x1+x2)%l==0:
        print('YES')
        print(0)
        exit()

if res == 1000000:
    print('NO')
else:
    print('YES')
    print(res)