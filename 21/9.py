from functools import reduce
from operator import mul
from collections import defaultdict

m = defaultdict(lambda: 9)
for y, l in enumerate(open(0)):
    for x, c in enumerate(l.strip()):
        m[y * 1j + x] = int(c)

lows = {}
for k, v in m.copy().items():
    if all(m[k + d] > v for d in (1, -1, 1j, -1j)):
        lows[k] = v
print(sum(lows.values()) + len(lows))

basins = []
for l in lows:
    s = [l]
    v = set()
    while s:
        c = s.pop(0)
        if c in v:
            continue
        v.add(c)

        for d in (1, -1, 1j, -1j):
            n = c + d
            if m[n] > m[c] and m[n] != 9:
                s.append(n)
    basins.append(len(v))
print(reduce(mul, sorted(basins)[-3 :]))
