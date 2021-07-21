import sys
from itertools import count

discs = []
for l in sys.stdin:
    l = l.strip()[:-1].split()
    discs.append((int(l[3]), int(l[-1])))

def get_first(discs):
    return next(t for t in count() if all((t + s + 1 + i) % p == 0 for i, (p, s) in enumerate(discs)))
    #t = 0
    #while True:
    #    if all((t + s + 1 + i) % p == 0 for i, (p, s) in enumerate(discs)):
    #        return t
    #    t += 1

print(get_first(discs), get_first(discs + [(11, 0)]))
