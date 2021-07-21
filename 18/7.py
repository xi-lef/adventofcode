import copy
import itertools
import string
import sys
from collections import defaultdict

lines = [l.split() for l in sys.stdin]

deps = defaultdict(set)
for l in lines:
    deps[l[-3]].add(l[1])
orig = copy.deepcopy(deps)

order = ''
ready = set(w for v in deps.values() for w in v) - set(deps.keys())
while ready:
    #print(ready)

    n = sorted(ready)[0]
    order += n
    ready.remove(n)

    for k, v in list(deps.items()):
        v.discard(n)
        if not v:
            ready.add(k)
            del deps[k]

print(order)

deps = orig
workers = [[0, ''] for _ in range(5)]
ready = set(w for v in deps.values() for w in v) - set(deps.keys())
for step in itertools.count(0):
    for i in range(len(workers)):
        if workers[i][0] != 0:
            workers[i][0] -= 1
            if workers[i][0] == 0:
                for k, v in list(deps.items()):
                    v.discard(workers[i][1])
                    if not v:
                        ready.add(k)
                        del deps[k]

    for i in range(len(workers)):
        if workers[i][0] == 0:
            if ready:
                n = sorted(ready)[0]
                order += n
                ready.remove(n)

                workers[i] = [string.ascii_uppercase.index(n) + 1 + 60, n]

    #print(step, ready, workers)
    if not ready and all(w[0] == 0 for w in workers):
        break
print(step)
