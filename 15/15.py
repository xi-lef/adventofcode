import sys
from functools import reduce
from operator import mul

ings = []
for l in sys.stdin:
    l = l.replace(',', '').split()
    ings.append(list(map(int, l[2:11:2])))

def combinations(ings, tsp):
    if not tsp:
        return
    if ings == 1:
        yield [tsp]
        return
    for i in range(tsp + 1):
        for c in combinations(ings - 1, tsp - i):
            yield [i] + c

m = h = 0
for comb in combinations(len(ings), 100):
    props = [[x * i for i in ing] for x, ing in zip(comb, ings)]
    props = [sum(x) for x in zip(*props)]
    score = reduce(mul, (max(0, x) for x in props[:-1]))
    m = max(m, score)
    if props[-1] == 500:
        h = max(h, score)

print(m, h)
