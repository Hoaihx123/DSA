def preprocess(pat):
    d = {}
    s = set()
    length = len(pat)
    for i in range(length-2, -1, -1):
        if pat[i] not in s:
            s.add(pat[i])
            d[pat[i]] = length - 1 - i
    if pat[-1] not in s:
        d[pat[-1]] = length
    d['*'] = length
    context = {'d': d, 's': s}
    return context
def BMH(pat, text):
    context = preprocess(pat)
    pat_length = len(pat)
    text_length = len(text)
    i = pat_length - 1
    j = pat_length - 1
    while (j >= 0) & (i < text_length):
        if pat[j] == text[i]:
            i -= 1
            j -= 1
        else:
            off = context['d'][text[i]] if context['d'].get(text[i], False) else context['d']['*']
            print(off)
            i += max(pat_length - j, off)
            j = pat_length - 1
    if j < 0:
        return i + 1

print(BMH('ABCABE', 'ABCABC ABCABCABE'))
