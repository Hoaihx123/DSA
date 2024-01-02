def palindrome(s):
    length = len(s)
    pal = [[False]*length for _ in range(length)]
    for i in range(length):
        pal[i][i] = True
    for L in range(2, length+1):
        for i in range(length - L + 1):
            j = i + L - 1
            if (s[i] == s[j]) and (L == 2 or pal[i+1][j-1]):
                pal[i][j] = True
    return pal
def min_cut(s):
    pal = palindrome(s)
    length = len(s)
    count = [length]*length
    for k in range(length):
        if pal[0][k]:
            count[k] = 0
        else:
            for i in range(k, 0, -1):
                if pal[i][k]:
                    count[k] = min(count[k], count[i-1] + 1)
    return count
print(min_cut('AAAAABABACAC'))
