import sys
from collections import Counter, defaultdict

O, T, L = range(3)
area = defaultdict(int)
for y, l in enumerate(sys.stdin):
    for x, c in enumerate(l):
        p = x + y * 1j
        if c == '|':
            area[p] = T
        elif c == '#':
            area[p] = L
s = int(max(x.real for x in area.keys())) + 1

def adj(area, p):
    t = l = 0
    for dx in (-1, 0, 1):
        for dy in (-1j, 0, 1j):
            if dx == dy == 0:
                continue
            v = area[p + dx + dy]
            t += v == T
            l += v == L
    return t, l

counts = []
i = last = 0
mins = 1000000000
while i < mins:
    new = area.copy()
    for x in range(s):
        for y in range(s):
            p = x + y * 1j
            v = area[p]
            t, l = adj(area, p)
            if v == O and t >= 3:
                new[p] = T
            elif v == T and l >= 3:
                new[p] = L
            elif v == L and (l == 0 or t == 0):
                new[p] = O
    area = new

    counter = Counter(area.values())
    val = counter[T] * counter[L]
    counts.append(val)
    if i == 9:
        print(val)

    diff = len(counts) - 1 - counts.index(val)
    if diff != 0 and diff == last:
        while i + diff < mins:
            i += diff
    i += 1
    last = diff

print(counts[-1])
