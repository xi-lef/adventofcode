import sys
from itertools import permutations

start = 0
locs = {}
open = set()
for y, l in enumerate(sys.stdin):
    for x, c in enumerate(l):
        p = x + y * 1j
        if c.isdecimal():
            if c == '0':
                start = p
            locs[p] = {}
        if c != '#':
            open.add(p)

def bfs(start, dists):
    stack = [(0, start)]
    while stack:
        dist, cur = stack.pop(0)
        if cur in dists:
            continue
        dists[cur] = dist

        for d in (-1, 1, -1j, 1j):
            new = cur + d
            if new in open:
                stack.append((dist + 1, new))

for p, dists in locs.items():
    bfs(p, dists)

for end in (None, start):
    shortest = 1e9
    for p in permutations(set(locs.keys()) - set([start])):
        p = (start, *p, end) if end else (start, *p)
        total = 0
        for i in range(len(p) - 1):
            total += locs[p[i]][p[i + 1]]
        shortest = min(shortest, total)
    print(shortest)
