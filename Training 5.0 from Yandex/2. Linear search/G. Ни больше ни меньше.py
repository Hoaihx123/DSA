k = int(input())
for _ in range(k):
    n = int(input())
    x = list(map(int, input().split()))
    i = 0
    s = ''
    q = 0
    while i < n:
        min_ = x[i]
        j = i+1
        check = True
        while j-i < min_ and j < n:
            if x[j] >= min_:
                j += 1
            else:
                if j-i < x[j]:
                    min_ = x[j]
                    j += 1
                else:
                    s += str(j-i)+' '
                    q += 1
                    i = j
                    check = False
                    break
        if check:
            s += str(j-i)+' '
            q += 1
            i = j
    print(q)
    print(s)