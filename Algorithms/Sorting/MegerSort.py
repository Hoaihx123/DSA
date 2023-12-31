def meger_list(a, b):
    N = len(a)
    M = len(b)
    c = [0]*(M+N)
    i = 0
    j = 0
    while i+j < M+N:
        if (i < N) & (j < M):
            if a[i] < b[j]:
                c[i+j] = a[i]
                i += 1
            else:
                c[i+j] = b[j]
                j += 1
        elif i == N:
            c[N+j] = b[j]
            j += 1
        else:
            c[M+i] = a[i]
            i += 1
    return c
def meger_sort(c, l, k):
    if l == k:
        return [c[l]]
    else:
        right = meger_sort(c, int((l+k+1)/2), k)
        left = meger_sort(c, l, int((l+k-1)/2))
        return meger_list(right, left)



c = [5, -8, 0, 9, 10, -3, 6, 2]

print(meger_sort(c, 0, len(c) - 1))