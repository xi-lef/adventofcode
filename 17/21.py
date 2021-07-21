import sys
from more_itertools import grouper

def rotate(p): return tuple(''.join(l) for l in zip(*p[:: -1]))

rules = {}
for line in sys.stdin:
    l, r = map(lambda p: tuple(p.split('/')), line.strip().split(' => '))
    for _ in range(4):
        rules[l] = r
        rules[l[:: -1]] = r
        l = rotate(l)

for r in (5, 18):
    grid = ['.#.', '..#', '###']
    for _ in range(r):
        new = []
        size = 2 if len(grid) % 2 == 0 else 3
        for rows in grouper(grid, size):
            newcols = []
            for cols in zip(*(grouper(r, size) for r in rows)):
                newcols.append(rules[tuple(''.join(t) for t in cols)])
            for r in (''.join(t) for t in zip(*newcols)):
                new.append(r)
        grid = new
    print(sum(r.count('#') for r in grid))
