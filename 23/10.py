pipes = {}
start = 0
for y, l in enumerate(open(0)):
    for x, c in enumerate(l.strip()):
        p = x + y * 1j
        if c == 'S':
            start = p
        pipes[p] = c

if pipes[start + 1] in '-J7':
    dir = 1
elif pipes[start - 1] in '-FL':
    dir =  -1
elif pipes[start + 1j] in '|JL':
    dir = 1j
else: # never entered, some other case must be true
    dir = -1j

loop = {start}
cur = start + dir
while cur != start:
    loop.add(cur)
    pipe = pipes[cur]
    match dir:
        case 1:
            dir = {'-': 1, 'J': -1j, '7': 1j}[pipe]
        case -1:
            dir = {'-': -1, 'F': 1j, 'L': -1j}[pipe]
        case 1j:
            dir = {'|': 1j, 'J': -1, 'L': 1}[pipe]
        case -1j:
            dir = {'|': -1j, 'F': 1, '7': -1}[pipe]
    cur += dir
print(len(loop) // 2)
