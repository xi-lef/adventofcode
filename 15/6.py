import sys
from collections import defaultdict

lines = [l.split() for l in sys.stdin]

lit = defaultdict(int)
bright = defaultdict(int)
for l in lines:
    start = [int(x) for x in l[-3].split(',')]
    end = [int(x) for x in l[-1].split(',')]

    for x in range(start[0], end[0] + 1):
        for y in range(start[1], end[1] + 1):
            p = (x, y)
            if l[0] == 'turn':
                on = l[1] == 'on'
                lit[p] = on
                bright[p] = max(0, bright[p] + (1 if on else -1))
            else:
                lit[p] ^= 1
                bright[p] += 2

print(len([k for k, v in lit.items() if v == 1]))
print(sum(bright.values()))
