w, h, n = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(n)]
a_1 = sorted(a, key=lambda x: x[0])
a_2 = sorted(a, key=lambda x: x[1])
def check(k):
    for point in a_1:
        l, r = 0, n
        while l < r:
            m = (r+l)//2
            if a_2[m][0]>=point[0] and a_2[m][0]<point[0]+k:
                l = m+1
            else:
                r = m
        index_l = l
        r = n-1
        while l < r:
            m = (l+r+1)//2
            if a_2[m][0] >= point[0] and a_2[m][0] < point[0] + k:
                r = m-1
            else:
                l = m
        index_r = l
        if index_r-index_l < k:
            print(index_r, index_l, point)
            return True
    return False

print(check(2))