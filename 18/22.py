import networkx as nx
from functools import cache

R, W, N = range(3)
depth = int(input().split()[1])
tx, ty = map(int, input().split()[1].split(','))
target = tx + ty * 1j
region = {}

@cache
def erosion(x, y):
    if (x == 0 and y == 0) or (x == tx and y == ty):
        g = 0
    elif y == 0:
        g = x * 16807
    elif x == 0:
        g = y * 48271
    else:
        g = erosion(x - 1, y) * erosion(x, y - 1)

    e = (g + depth) % 20183
    region[x + y * 1j] = e % 3
    return e

for x in range(tx + 1):
    for y in range(ty + 1):
        erosion(x, y)
print(sum(region.values()))

for x in range(tx + 100):
    for y in range(ty + 100):
        erosion(x, y)

NO, CG, TO = range(3)
allowed = {R: (CG, TO), W: (CG, NO), N: (TO, NO)}

g = nx.Graph()
# TODO why is this slightly wrong
#g.add_node((0, TO))
#for pos in region:
#    for dir in (1, -1, 1j, -1j):
#        npos = pos + dir
#        if npos not in region:
#            continue
#        for apos in allowed[region[pos]]:
#            for anpos in allowed[region[npos]]:
#                g.add_edge((pos, apos), (npos, anpos), weight = 1 if apos == anpos else 8)
for pos in region:
    apos = allowed[region[pos]]
    g.add_edge((pos, apos[0]), (pos, apos[1]), weight = 7)
    for dir in (1, -1, 1j, -1j):
        npos = pos + dir
        if npos not in region:
            continue
        for a in set(apos) & set(allowed[region[npos]]):
            g.add_edge((pos, a), (npos, a), weight = 1)
print(nx.shortest_path_length(g, (0, TO), (target, TO), 'weight'))

#from collections import defaultdict
#times = defaultdict(lambda: 1e9)
#stack = [(0, TO, 0)]
#while stack:
#    p, g, t = stack.pop()
#    #print(p, g, t)
#    if p == target:
#        if g != TO:
#            g = TO
#            t += 7
#        print(t)
#
#    if times[p, g] <= t:
#        continue
#    times[p, g] = t
#
#    if p not in region:
#        continue
#
#    cr = region[p]
#    for dir in (1, -1, 1j, -1j):
#        n = p + dir
#        if n not in region:
#            continue
#
#        nr = region[n]
#        #print(n, nr)
#        if nr == cr:
#            stack.append((n, g, t + 1))
#        else:
#            for ng in allowed[nr]:
#                stack.append((n, ng, t + 1 if ng == g else t + 8))
#print(times[target, TO])
