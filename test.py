from filecmp import cmp

x1 = [[input(), input()] for _ in range(40)]
x2 = [[input(), input()] for _ in range(40)]
for i in range(40):
    if x1[i][1][0:len(x1[i][1])-1] != x2[i][1] or x1[i][0]!=x2[i][0]:
        print(x1[i], x2[i])
