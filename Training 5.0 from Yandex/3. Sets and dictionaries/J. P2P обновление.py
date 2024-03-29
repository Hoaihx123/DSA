n, k = list(map(int, input().split()))
devices = [{'updated_section': set(), 'requests': []} for _ in range(n)]
devices[0]['updated_section'] = {i for i in range(k)}
sections = [[0, ] for i in range(k)]
priority = [[0 for _ in range(n)] for _ in range(n)]
res = {}
temp = [i for i in range(k)]
num = 0
while len(res) < n-1:
    num += 1
    temp_ = sorted(temp, key=lambda a: len(sections[a]))
    for i in range(1, n):
        if len(devices[i]['updated_section']) < k:
            for section in temp_:
                if section not in devices[i]['updated_section']:
                    break
            device_to_request = 0
            for d in sections[section]:
                if len(devices[d]['updated_section']) < len(devices[device_to_request]['updated_section']):
                    device_to_request = d
                elif len(devices[d]['updated_section']) == len(devices[device_to_request]['updated_section']):
                    if d < device_to_request:
                        device_to_request = d
            devices[device_to_request]['requests'].append([i, section])
    update = []
    for i in range(n):
        if len(devices[i]['requests']) > 0:
            devices_to_update = devices[i]['requests'][0]
            for x in devices[i]['requests']:
                if priority[i][x[0]] > priority[i][devices_to_update[0]]:
                    devices_to_update = x
                elif priority[i][x[0]] == priority[i][devices_to_update[0]]:
                    if len(devices[x[0]]['updated_section']) < len(devices[devices_to_update[0]]['updated_section']):
                        devices_to_update = x
            update.append([i, devices_to_update[0], devices_to_update[1]])
            devices[i]['requests'] = []
    for u in update:
        devices[u[1]]['updated_section'].add(u[2])
        sections[u[2]].append(u[1])
        priority[u[1]][u[0]] += 1
        if len(devices[u[1]]['updated_section']) >= k:
            res[u[1]] = num

for i in range(1, n):
    print(res[i], end=' ')





