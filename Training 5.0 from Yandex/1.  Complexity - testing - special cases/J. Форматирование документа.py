import re
import sys
def add_line(s, arr):
    matches = list(re.finditer('\(image [^\)]+\)', s))
    start = 0
    for x in matches:
        arr += s[start: x.start()].split()
        arr.append(x.group())
        start = x.end()
    arr += s[start:].split()

w, h, c = list(map(int, input().split()))

paragraphs = [[]]
lines = sys.stdin.readlines()
st = ''
for s in lines:
    if not s.strip():
        add_line(st, paragraphs[-1])
        paragraphs.append([])
        st = ''
    else:
        st += ' '+ s.strip()
add_line(st, paragraphs[-1])
cur = [0, 0]
sur_images = []
fl = [0, 0]
for paragraph in paragraphs:
    index_in_sur = 0
    i = 0
    line_height = h
    check = False
    is_floating = False
    while i < len(paragraph):
        if cur[0] == 0:
            j = 0
            while j < len(sur_images):
                if sur_images[j][2] <= cur[1]:
                    sur_images.pop(j)
                else:
                    j += 1
        word = paragraph[i]
        if re.search("\(image [^\)]+\)", word):
            type_of_image = re.findall(' layout=(\w+)[\s)]', word)[0]
            width = int(re.findall('width=(\d+)\s*[)\s]', word)[0])
            height = int(re.findall('height=(\d+)\s*[)\s]', word)[0])
            if type_of_image == 'surrounded':
                is_floating = False
                length_ = width
                if index_in_sur >= len(sur_images):
                    if cur[0] + length_ <= w:
                        print(cur[0], cur[1])
                        sur_images.append([cur[0], cur[0]+length_, cur[1]+height])
                        cur[0] += length_
                        i += 1
                        check = True
                    else:
                        cur[0] = 0
                        cur[1] += line_height
                        line_height = h
                        index_in_sur = 0
                        check = False
                else:
                    if cur[0] + length_ <= sur_images[index_in_sur][0]:
                        print(cur[0], cur[1])
                        sur_images.insert(index_in_sur, [cur[0], cur[0]+length_, cur[1]+height])
                        cur[0] += length_
                        i += 1
                    else:
                        cur[0] = sur_images[index_in_sur][1]
                        index_in_sur += 1
                    check = True

            elif type_of_image == 'floating':
                if is_floating:
                    cur_ = fl
                else:
                    cur_ = cur
                dx = int(re.findall('dx=(-?\d+)\s*[)\s]', word)[0])
                dy = int(re.findall('dy=(-?\d+)\s*[)\s]', word)[0])
                y = dy + cur_[1]
                x = cur_[0]+dx
                if x+width > w:
                    x = w - width
                if x < 0:
                    x = 0
                print(x, y)
                fl = [x+width, y]
                i += 1
                is_floating =True
            elif type_of_image == 'embedded':
                is_floating = False
                length_ = width
                if cur[0] != 0:
                    cur[0] += c
                if check:
                    cur[0] -= c
                if index_in_sur >= len(sur_images):
                    if cur[0] + length_ <= w:
                        print(cur[0], cur[1])
                        cur[0] += length_
                        i += 1
                        line_height = max(line_height, height)
                        check = False
                    else:
                        cur[0] = 0
                        cur[1] += line_height
                        line_height = h
                        index_in_sur = 0
                        check = False
                else:
                    if cur[0] + length_ <= sur_images[index_in_sur][0]:
                        print(cur[0], cur[1])
                        cur[0] += length_
                        line_height = max(line_height, height)
                        i += 1
                        check = False
                    else:
                        cur[0] = sur_images[index_in_sur][1]
                        index_in_sur += 1
                        check = True
        else:
            is_floating = False
            length_ = len(word)
            if cur[0] != 0:
                cur[0] += c
            if check:
                cur[0] -= c
            if index_in_sur >= len(sur_images):
                if cur[0]+length_*c <= w:
                    cur[0] += length_*c
                    i += 1
                    check = False
                else:
                    cur[0] = 0
                    cur[1] += line_height
                    line_height = h
                    index_in_sur = 0
                    check =False
            else:
                if cur[0]+length_*c <= sur_images[index_in_sur][0]:
                    cur[0] += length_*c
                    i += 1
                    check = False
                else:
                    cur[0] = sur_images[index_in_sur][1]
                    index_in_sur += 1
                    check = True
    cur[0] = 0
    cur[1] += line_height

    # re.findall(' layout=(.+)\s*[)\s]', word)[0]





