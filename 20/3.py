import sys
from functools import reduce
from operator import mul

trees = [l.strip() for l in sys.stdin]

enc = []
for dx, dy in ((3, 1), (1, 1), (5, 1), (7, 1), (1, 2)):
    c = 0
    for y, l in enumerate(trees[::dy]):
        c += l[y * dx % len(l)] == '#'
    enc.append(c)

print(enc[0], reduce(mul, enc))
