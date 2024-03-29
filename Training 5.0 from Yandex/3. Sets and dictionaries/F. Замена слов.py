vocalbs = input().split()
tree = {}
for s in vocalbs:
    cur = tree
    for c in s:
        if c not in cur:
            cur[c] = {}
        cur = cur[c]
    cur[''] = {}
words = input().split()
for word in words:
    cur = tree
    i = 0
    for c in word:
        if c not in cur or '' in cur:
            break
        else:
            cur = cur[c]
        i += 1
    if '' in cur:
        print(word[:i], end=' ')
    else:
        print(word, end=' ')
