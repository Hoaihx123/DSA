import sys
sys.setrecursionlimit(10**5)

x = int(input())
y = int(input())
p = int(input())
m = (1+5**(1/2))/2
def recursive(x, y, p, q):
    res_1, res_2 = 1000000, 1000000
    if x <= 0:
        return 1000000
    if y <= 0 and q <= 0:
        return 0
    if x > q:
        q_ = 0
        y_ = max(y-x+q, 0)
        if y_ > 0:
            q_ += p
        res_1 = recursive(x, y_, p, q_)
    if x >= y:
        q_ = max(0, q-x+y)
        x_ = x-q_
        res_2 = recursive(x_, 0, p, q_)
    return 1+min(res_1, res_2)

res = recursive(x, y, p, 0)
if res >= 1000000:
    print(-1)
else:
    print(res)
#
