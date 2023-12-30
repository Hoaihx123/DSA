def computeLPSArray(pat): #the longest proper prefix
    length = len(pat)
    lps = [0]*length
    j = 0
    lps[0] = 0
    i = 1
    while i < length:
        if pat[i] == pat[j]:
            lps[i] = j+1
            i += 1
            j += 1
        elif j == 0:
            lps[i] = 0
            i += 1
        else:
            j = lps[j-1]
    return lps
def searchKMP(pat, txt):
    i = 0
    j = 0
    txt_length = len(txt)
    pat_length = len(pat)
    lps = computeLPSArray(pat)
    while (i <= txt_length - pat_length) & (j < pat_length):
        if txt[i+j] == pat[j]:
            j += 1
        else:
            if j:
                i = i + j - lps[j-1]
                j = lps[j-1]
            else:
                i += 1
    if j == pat_length:
        return i
    return -1
pat = 'ABDAC'
print(computeLPSArray(pat))
txt = 'ABAA ABDADAC'
print(txt)
print(searchKMP(pat, txt))