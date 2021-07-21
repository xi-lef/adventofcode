import sys
from collections import defaultdict

bots = {}
for l in sys.stdin:
    p, r = l[5:].strip().split('>, r=')
    x, y, z = map(int, p.split(','))
    bots[x, y, z] = int(r)

def dist(a, b):
    return sum(map(lambda v: abs(v[0] - v[1]), zip(a, b)))

pos, rad = max(bots.items(), key = lambda b: b[1])
c = 0
for other in bots:
    if dist(pos, other) <= rad:
        c += 1
print(c)

overlaps = defaultdict(set)
for b, r in bots.items():
    for o, r2 in bots.items():
        if dist(b, o) < r + r2:
            overlaps[b].add(o)

#print(sorted([(b, len(o)) for b, o in overlaps.items()], key = lambda t: t[1], reverse = True))
