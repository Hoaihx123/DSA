matrix = [input() for _ in range(8)]
s = set()
for i in range(8):
    for j in range(8):
        if matrix[i][j] == 'R':
            s.add((i, j))
            t = j-1
            while t >= 0:
                s.add((i, t))
                if matrix[i][t] != '*':
                    break
                t -= 1
            t = j+1
            while t <= 7:
                s.add((i, t))
                if matrix[i][t] != '*':
                    break
                t += 1
            t = i-1
            while t >= 0:
                s.add((t, j))
                if matrix[t][j] != '*':
                    break
                t -= 1
            t = i+1
            while t <= 7:
                s.add((t, j))
                if matrix[t][j] != '*':
                    break
                t += 1
        elif matrix[i][j] == 'B':
            s.add((i, j))
            t = 1
            while i-t >= 0 and j+t <= 7:
                s.add((i-t, j+t))
                if matrix[i-t][j+t] != '*':
                    break
                t += 1
            t = 1
            while i-t >= 0 and j-t >= 0:
                s.add((i-t, j-t))
                if matrix[i-t][j-t] != '*':
                    break
                t += 1
            t = 1
            while i + t <= 7 and j + t <= 7:
                s.add((i + t, j + t))
                if matrix[i + t][j + t] != '*':
                    break
                t += 1
            t = 1
            while i + t <= 7 and j - t >= 0:
                s.add((i + t, j - t))
                if matrix[i + t][j - t] != '*':
                    break
                t += 1

print(64-len(s))