wordDict = ["cat","cats","and","sand","dog"]
root ={}

for word in wordDict:
    cur =root
    for c in word:
        if c not in cur:
            cur[c ] ={}
        cur =cur[c]
    cur['']={}
def dp(s,k,n):
    cur=root
    result=[]
    for i in range(k, n):
        if '' in cur:
            x=dp(s, i, n)
            if x:
                for r in x:
                    print(r)
                    result.append(s[k:i]+' '+r)
        if s[i] in cur:
            cur=cur[s[i]]
        else:
            return result
    if '' in cur:
        result.append(s[k:])
    return result

s = "catsanddog"
n=len(s)
print(dp(s,0,n))
