n = int(input())
def check(k, n):
    return k*(k+1)//2 < n
l, r = 0, n
while l < r:
    m = (l+r+1)//2
    if check(m, n):
        l = m
    else:
        r = m-1
if l%2:
    s = str(l+2-n+(l*(l+1)//2))+'/'+str(n-(l*(l+1)//2))
else:
    s = str(n-(l*(l+1)//2))+'/'+str(l+2-n+(l*(l+1)//2))
print(s)