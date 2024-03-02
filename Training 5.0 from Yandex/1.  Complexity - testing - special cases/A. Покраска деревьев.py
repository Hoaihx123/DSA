def solution(p, v, q, m):
    if p+v < q-m:
        return 2*v+2*m+2
    return max(2*v+1, 2*m+1, q+m-p+v+1)


p, v = map(int, input().split())
q, m = map(int, input().split())
if p<q:
    print(solution(p,v,q,m))
else:
    print(solution(q,m,p,v))