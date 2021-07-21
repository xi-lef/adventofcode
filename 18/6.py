#import numpy as np
import sys
from collections import Counter

points = [tuple(int(x) for x in l.split(', ')) for l in sys.stdin]

max_x = max([t[0] for t in points])
max_y = max([t[1] for t in points])

def nearest(x, y):
    md = max_x + max_y
    mp = -1
    total = 0
    for p, (px, py) in enumerate(points):
        dist = abs(px - x) + abs(py - y)
        if dist < md:
            md = dist
            mp = p
        elif dist == md:
            mp = -1
        total += dist
    return mp, total < 10000

grid = {}
#grid = np.empty((max_x + 1, max_y + 1))
safe = set()
for x in range(max_x + 1):
    for y in range(max_y + 1):
        n, all = nearest(x, y)
        grid[(x, y)] = n
        if all:
            safe.add((x, y))

count = Counter(grid.values())
#count = Counter()
#for r in grid.tolist(): count.update(r)

del count[-1]
for x in range(max_x + 1):
    count.pop(grid[(x, 0)], 0)

    if x in (0, max_x):
        for y in range(max_y):
            count.pop(grid[(x, y)], 0)

    count.pop(grid[(x, max_y)], 0)

print(count.most_common(1), len(safe))
