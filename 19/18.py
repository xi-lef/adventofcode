import string
import sys
from collections import defaultdict, deque

start = 0
open = set()
keys = {}
doors = {}

for y, l in enumerate(sys.stdin):
    for x, c in enumerate(l):
        p = x + y * 1j
        if c == '@':
            start = p
            open.add(p)
        elif c == '.':
            open.add(p)
        elif c in string.ascii_lowercase:
            keys[p] = c
        elif c in string.ascii_uppercase:
            doors[p] = c.lower()

good = 1e9
dists = defaultdict(lambda: 1e9)
stack = deque([(start, frozenset(), 0)])
while stack:
    p, k, s = e = stack.popleft()

    if p in keys:
        k = k | frozenset(keys[p])
    #print(p, k, s)

    if len(k) == len(keys):
        good = min(good, s)
        continue
    if dists[(p, k)] <= s:
        continue
    dists[(p, k)] = s

    for d in (1, -1, 1j, -1j):
        n = p + d
        if n in open or n in keys or (n in doors and doors[n] in k):
            stack.append((n, k, s + 1))
print(good)

open.remove(start)
for d in (1, -1, 1j, -1j):
    open.remove(start + d)
starts = (start + 1 + 1j, start + 1 - 1j, start - 1 - 1j, start - 1 + 1j)

good = 1e9
dists = defaultdict(lambda: 1e9)
stack = deque([(starts, frozenset(), 0)])
while stack:
    ps, k, s = e = stack.popleft()

    for p in ps:
        if p in keys:
            k = k | frozenset(keys[p])
    #print(p, k, s)

    if len(k) == len(keys):
        good = min(good, s)
        continue
    if dists[(ps, k)] <= s:
        continue
    dists[(ps, k)] = s

    for i, p in enumerate(ps):
        for d in (1, -1, 1j, -1j):
            n = p + d
            if n in open or n in keys or (n in doors and doors[n] in k):
                ns = list(ps)
                ns[i] = n
                stack.append((tuple(ns), k, s + 1))
print(good)
