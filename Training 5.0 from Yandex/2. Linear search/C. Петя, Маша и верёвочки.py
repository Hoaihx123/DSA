n = int(input())
x = list(map(int, input().split()))
max_l = 0
sum_l = 0
for l in x:
    if l > max_l:
        sum_l += max_l
        max_l = l
    else:
        sum_l += l
if sum_l < max_l:
    print(max_l-sum_l)
else:
    print(sum_l+max_l)