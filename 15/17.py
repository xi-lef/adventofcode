import sys
from itertools import combinations

sizes = {i: int(l) for i, l in enumerate(sys.stdin)}

#visited = set()
#combs = set()
#def fill(cons, rem):
#    if rem == 0:
#        combs.add(frozenset(cons))
#
#    for i, s in ((i, s) for i, s in sizes.items() if s <= rem and i not in cons):
#        new = cons | {i}
#        if new not in visited:
#            fill(new, rem - s)
#    visited.add(frozenset(cons))
#fill(set(), 150)

combs = [c for i in range(len(sizes)) for c in combinations(sizes.values(), i) if sum(c) == 150]
print(len(combs), len(min(combs, key = lambda x: len(x))))
