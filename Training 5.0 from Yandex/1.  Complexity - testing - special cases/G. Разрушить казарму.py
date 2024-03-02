# x = int(input())
# y = int(input())
# p = int(input())
# Не прошел
x = 25
y = 200
p = 10
def recusive(x, y, q):
    if y <= 0:
        res = 0
        while x > 0 and q > 0:
            q -= x
            x -= q
            res += 1
        if x > 0:
            return res
        return 1000000
    else:
        q += p
        high = min(2*x-q, x, y)+1
        low = max(1, x-q)
        res = 1000000

        for k in range(low, high):
            y_ = y-k
            q_ = max(q-x+k, 0)
            x_ = x - q_

            res = min(res, 1+recusive(x_, y_, q_))
            print(x_, y_, q_, res)
        return res
print(1+recusive(25, 175, 0))


