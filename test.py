s="barfoothefoobarman"
words=["foo","bar"]

m = len(words[0])
n = len(words)
l = len(s)
dict1 = {}
result = []
for w in words:
    dict1[w] = dict1.get(w, 0) + 1
for i in range(m):
    start = i
    while start + m * n <= l:
        dict2 = {}
        j=start
        while j <start+m*n:
            if dict1.get(s[j:j + m], 0) > dict2.get(s[j:j + m], 0):
                dict2[s[j:j + m]] = dict2.get(s[j:j + m], 0) + 1
                j+=m
            else:
                break
        print(j)
        if j < start + m * n:
            if dict1.get(s[j:j + m]):
                start += m
            else:
                start = j + m
        else:
            result.append(start)
            start += m
print(result)

