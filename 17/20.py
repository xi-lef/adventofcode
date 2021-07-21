import sys
from collections import Counter
from copy import deepcopy

parts = {}
for i, l in enumerate(sys.stdin):
    p, v, a = l.strip().split(', ')
    p, v, a = map(lambda x: x[3 : -1].split(','), (p, v, a))
    parts[i] = tuple(tuple(map(int, x)) for x in (p, v, a))

def sim(parts, collide = False):
    m = reps = 0
    while reps < 1000:
        count = Counter()
        for i, (p, v, a) in parts.items():
            v = tuple(vi + ai for vi, ai in zip(v, a))
            p = tuple(pi + vi for pi, vi in zip(p, v))
            parts[i] = (p, v, a)
            count.update([p])

        if collide:
            parts = {i: t for i, t in parts.items() if count[t[0]] == 1}

        dists = {i: sum(abs(x) for x in t[0]) for i, t in parts.items()}
        nm = min(dists, key = dists.get)
        if m == nm:
            reps += 1
        m = nm

    return parts, m

print(sim(deepcopy(parts))[1])
print(len(sim(parts, True)[0]))
