def solve(s):
    d = {}
    for x in s:
        if x not in d:
            d[x] = 1
        else:
            d[x] += 1
    return d
s_1 = input()
s_2 = input()
if solve(s_1) == solve(s_2):
    print('YES')
else:
    print('NO')