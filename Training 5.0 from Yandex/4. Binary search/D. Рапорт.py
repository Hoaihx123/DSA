w, n, m = list(map(int, input().split()))
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
def count_line(arr, wight):
    res = 1
    current_line = 0
    for word_line in arr:
        if word_line > wight:
            return float('inf')
        if current_line+word_line > wight:
            res += 1
            current_line = word_line+1
        else:
            current_line += word_line+1
    return res
l, r = 0, w
while l < r:
    m = (l+r)//2
    if count_line(a1, m) > count_line(a2, w - m):
        l = m+1
    else:
        r = m
print(min(count_line(a2, w-l), count_line(a1, l-1)))


