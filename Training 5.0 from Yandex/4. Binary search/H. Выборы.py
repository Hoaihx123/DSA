n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a_ = [a[i].copy() for i in range(n)]
for i in range(n):
    a[i].append(i)
a.sort(key=lambda x: (x[0], x[1] if x[1] != -1 else float('inf')))
a.append([0, 0, n])
for i in range(n):
    a[i][0] += a[i-1][0]

def solve(start, j):
    if j == n-1:
        return a_[a[j][2]][0]
    s = a[n-1][0]-a[start-1][0]+a_[a[j][2]][0]
    k = s//(n-start+1)+1
    if s % (n-start+1) > 1:
        k += 1
    return k
res = [float('inf'), 0, 0]
for i in range(n):
    if i > 0 and a_[a[i][2]][0] == a_[a[i-1][2]][0]:
        continue
    if a[i][1] != -1:
        l, r = i+1, n-1
        while l < r:
            m = (l+r+1)//2
            if solve(m, i) > a_[a[m-1][2]][0]:
                l = m
            else:
                r = m-1
        s = solve(l, i)
        if s-a_[a[i][2]][0]+a[i][1] < res[0]:
            res = [s-a_[a[i][2]][0]+a[i][1], i, l]
print(res[0])
print(a[res[1]][2]+1)
s = a[n-1][0]-a[res[2]-1][0]+a_[a[res[1]][2]][0]
k = s//(n-res[2]+1)
c = s % (n-res[2]+1)
for i in range(res[2], n):
    a_[a[i][2]][0] = k
a_[a[res[1]][2]][0] = k+1
if c == 0:
    a_[a[n-1][2]][0] -= 1
elif c > 1:
    a_[a[res[1]][2]][0] += 1
    for i in range(c-2):
        a_[a[n-i-1][2]][0] += 1
for x in a_:
    print(x[0], end=' ')

