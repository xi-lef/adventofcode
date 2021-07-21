from collections import defaultdict
import sys

lines = [l.strip() for l in sys.stdin]

conns = defaultdict(list)
for l in lines:
    r, d = l.split(' = ')
    a, b = r.split(' to ')
    conns[a].append((b, (int(d))))
    conns[b].append((a, (int(d))))

#print(conns)
cities = set(conns.keys())
#print(cities)
n = len(cities)
all = []

def test(path):
    #print(path)
    if len(path) == n:
        all.append((path, path[-1][1]))
        return

    visited = set(c for c, _ in path)
    last, lastd = path[-1]
    for next, nextd in conns[last]:
        if next not in visited:
            test(path + [(next, lastd + nextd)])

for c in cities:
    test([(c, 0)])

print(min(all, key = lambda t: t[1])[1])
print(max(all, key = lambda t: t[1])[1])
