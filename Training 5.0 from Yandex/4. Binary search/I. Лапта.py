d, n = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]
EPS = 1e-6
def check_point_in_circle(x1, y1, r1, x, y):
    # if (x-x1)**2+(y-y1)**2 < r1*r1-0.000000001:
    #     return True
    # if (x - x1) ** 2 + (y - y1) ** 2 > r1 * r1 + 0.000000001:
    #     return False
    # else:
    return (x - x1) ** 2 + (y - y1) ** 2 < r1 * r1
def circle_intersection(x1, y1, r1, x2, y2, r2):
    if y1==y2:
        x = (r1*r1-r2*r2+x2*x2+y2*y2-x1*x1-y1*y1)/(2*(x2-x1))
        delta = r1*r1-(x-x1)**2
        if delta < 0:
            return []
        if delta == 0:
            return [[x, y1]]
        return [[x, y1-delta**0.5], [x, y1+delta**0.5]]
    a = -(x2-x1)/(y2-y1)
    b = (r1*r1-r2*r2+x2*x2+y2*y2-x1*x1-y1*y1)/(2*(y2-y1))
    a_ = 1+a**2
    b_ = x1+a*y1-a*b
    c_ = x1*x1+(b-y1)**2-r1*r1
    delta = b_*b_-a_*c_
    if delta < 0:
        return []
    if delta == 0:
        x = b_/a_
        y = a*x+b
        return [[x, y]]
    else:
        x_1 = (b_+delta**0.5)/a_
        x_2 = (b_-delta**0.5)/a_
        return [[x_1, a*x_1+b], [x_2, a*x_2+b]]

def check(t):
    circles = []
    points = []
    for x, y, v in arr:
        r = t*v
        intersections = circle_intersection(0, 0, d, x, y, r)
        if len(intersections) <= 1:
            if check_point_in_circle(0, 0, d, x, y):
                if r > d:
                    return False
                else:
                    circles.append([x, y, r])
                    if len(intersections):
                        if intersections[0][1] >= 0:
                            points.append(intersections[0])
            elif check_point_in_circle(x, y, r, 0, 0):
                return False
        else:
            s = 0
            for inter in intersections:
                if inter[1] >= 0:
                    points.append(inter)
                    s += 1
            if s == 0:
                return False
            circles.append([x, y, r])
    for x, y in points:
        b = True
        for x1, y1, r1 in circles:
            if check_point_in_circle(x1, y1, r1, x, y):
                b = False
                break
        if b:
            return [x, y]
    points = []
    for i in range(len(circles)):
        x1, y1, r1 = circles[i]
        if r1 > y1:
            x_1 = x1 + (r1 ** 2 - y1 ** 2) ** 0.5
            x_2 = x1 - (r1 ** 2 - y1 ** 2) ** 0.5
            if -d <= x_1 <= d:
                points.append([x_1, 0])
            if -d <= x_2 <= d:
                points.append([x_2, 0])
    for i in range(len(circles)-1):
        x1, y1, r1 = circles[i]
        for j in range(i+1, len(circles)):
            x2, y2, r2 = circles[j]
            intersections = circle_intersection(x1, y1, r1, x2, y2, r2)
            for x, y in intersections:
                if y >= 0 and x**2+y**2 <= d**2:
                    points.append([x, y])
    if len(points) == 0:
        return [0, d]
    for x, y in points:
        b = True
        for x1, y1, r1 in circles:
            if (x-x1)**2+(y-y1)**2 < (r1-0.000001)**2:
                b = False
                break
        if b:
            return [x, y]
    return False
max_t = 0
for x, y, v in arr:
    if (x*x+y*y+d*d)/(v*v) > max_t:
        max_t = (x*x+y*y+d*d)/(v*v)
max_t = max_t**0.5
left, right = 0, max_t
while right-left > 0.000001:
    mid = (left+right)/2
    if check(mid):
        left = mid
    else:
        right = mid
print(round(left, 4))
res = check(left)
print(round(res[0], 4), round(res[1], 4))


