from collections import defaultdict
import math
import sys

grid = []
for l in sys.stdin:
    grid.append(list(l.strip('\n')))

def count(g, x, y):
    #c = 0
    #n = len(g)
    #r = [*range(n), *range(0, -n, -1)]
    #for dx in r:
    #    for dy in r:
    #        nx = x + dx
    #        ny = y + dy
    #        if nx not in range(n) or ny not in range(n) or nx == x and ny == y:
    #            continue
    #        first = True
    #        m = 1
    #        while (a := x + m * dx) in range(n) and (b := y + m * dy) in range(n):
    #            if g[b][a] == '#':
    #                c += first
    #                first = False
    #                g[b][a] = '.'
    #            m += 1

    n = len(g)
    d = defaultdict(list)
    for a in range(n):
        for b in range(n):
            if a == x and b == y:
                continue
            if g[b][a] == '#':
                dx = a - x
                dy = b - y
                angle = (math.atan2(dy, dx) / math.pi * 180 + 450) % 360
                dist = math.sqrt(dx ** 2 + dy ** 2)
                d[angle].append((dist, a, b))

    #map(lambda l: l.sort(key = lambda t: t[0]), d.values())
    for v in d.values():
        v.sort(key = lambda t: t[0])
    angles = list(d.keys())
    angles.sort()
    cur = 0
    for _ in range(199):
        while not d[angles[cur]]:
            cur = (cur + 1) % len(angles)
        d[angles[cur]].pop(0)
        cur = (cur + 1) % len(angles)

    return len(d), d[angles[cur]]

m = mx = my = 0
for y, l in enumerate(grid):
    for x, p in enumerate(l):
        if p == '#':
            c, _ = count([g[:] for g in grid], x, y)
            if c > m:
                m = c
                mx = x
                my = y
print(m)

asteroid = count(grid, mx, my)[1][0]
print(asteroid[1] * 100 + asteroid[2])
