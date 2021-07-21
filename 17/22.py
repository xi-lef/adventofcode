import sys
from collections import defaultdict

C, W, I, F, M = range(5)
grid = defaultdict(int)
for y, l in enumerate(sys.stdin):
    for x, c in enumerate(l):
        if c == '#':
            grid[x + y * 1j] = I

cur = int(max(x.real for x in grid)) // 2
cur += cur * 1j
cur_ = cur

grid2 = grid.copy()
dir = -1j
c = 0
for _ in range(10000):
    g = grid[cur]
    c += not g
    grid[cur] = not g

    dir *= 1j if g else -1j
    cur += dir
print(c)

grid = grid2
cur = cur_
dir = -1j
c = 0
for _ in range(10000000):
    g = grid[cur]
    c += g == W
    grid[cur] = (g + 1) % M

    dir *= {C: -1j, W: 1, I: 1j, F: -1}[g]
    cur += dir
print(c)
