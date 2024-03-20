m, n = list(map(int, input().split()))
a = [input() for _ in range(m)]

right = None
left = None
for i in range(m):
    count = []
    start = -1
    end = -1
    for j in range(n):
        if a[i][j] == '#' and end >= start:
            start = j
        elif a[i][j] == '.' and end < start:
            end = j
            count.append([start, end])
    if start > end:
        count.append([start, n])
    if len(count) > 2:
        print('NO')
        exit()
    if len(count) == 2:
        if left is None:
            left = [count[0], [i, i], False]
            right = [count[1], [i, i], False]
        elif right is None:
            if left[2]:
                print('NO')
                exit()
            if left[0] == count[0]:
                right = [count[1], [i, i], False]
                left[1][1] = i
            elif left[0] == count[1]:
                right = left
                left = [count[1], [i, i], False]
                right[1][1] = i
            else:
                print('NO')
                exit()
        else:
            if left[2] == False and left[0] == count[0] and right[2] == False and right[0] == count[1]:
                left[1][1] = i
                right[1][1] = i
            else:
                print('NO')
                exit()
    elif len(count) == 1:
        if left is None:
            left = [count[0], [i, i], False]
        elif right is None:
            if left[2] == False and left[0] == count[0]:
                left[1][1] = i
            elif left[2] == False and (left[0][0]==count[0][0] or left[0][1]==count[0][1]) and (left[0][1]-left[0][0]<count[0][1]-count[0][0]):
                if left[0][0] == count[0][0]:
                    left[1][1] = i
                    right = [[left[0][1], count[0][1]], [i, i], False]
                else:
                    right = left
                    right[1][1] = i
                    left = [[count[0][0], right[0][0]], [i, i], False]
            else:
                left[2] = True
                right = [count[0], [i, i], False]
        else:

            if left[2] == False and left[0] == count[0]:
                left[1][1] = i
                right[2] = True
            elif right[2] == False and right[0] == count[0]:
                right[1][1] = i
                left[2] = True
            elif left[2] == False and right[2] == False and left[0][0]==count[0][0] and right[0][1]==count[0][1] and left[0][1]==right[0][0]:
                left[1][1] = i
                right[1][1] = i
            else:
                print('NO')
                exit()
    else:
        if right is not None:
            left[2] = True
            right[2] = True
        elif left is not None:
            left[2] = True
if left is None:
    print('NO')
    exit()
if right is None:
    if left[2] == False:
        left[1][1] = m-1
    if left[0][0] < left[0][1]-1:
        for i in range(left[1][0], left[1][1]+1):
            a[i] = a[i][:left[0][0]]+'a'+'b'*(left[0][1]-1-left[0][0]) + a[i][left[0][1]:]
    elif left[1][0] < left[1][1]:
        a[left[1][0]] = a[left[1][0]][:left[0][0]]+'a'+a[left[1][0]][left[0][0]+1:]
        for i in range(left[1][0]+1, left[1][1]+1):
            a[i] = a[i][:left[0][0]]+'b'+a[i][left[0][0]+1:]
    else:
        print('NO')
        exit()
else:
    if left[2] == False:
        left[1][1] = m-1
    if right[2] == False:
        right[1][1] = m-1
    for i in range(left[1][0], left[1][1]+1):
        a[i] = a[i][:left[0][0]]+'a'*(left[0][1]-left[0][0])+a[i][left[0][1]:]
    for i in range(right[1][0], right[1][1]+1):
        a[i] = a[i][:right[0][0]]+'b'*(right[0][1]-right[0][0])+a[i][right[0][1]:]
print('YES')
print('\n'.join(a))