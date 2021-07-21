import numpy as np
import operator
import sys

#dirs = {'e': (1,  0), 'se': (0, -1), 'sw': (-1, -1),
#        'w': (-1, 0), 'nw': (0, 1), 'ne': (1, 1)}
dirs = {'e': 1, 'se': -1j, 'sw': -1 - 1j,
        'w': -1, 'nw': 1j, 'ne':  1 + 1j}

lines = []
for l in sys.stdin:
    l = l.rstrip('\n')
    d = []
    i = 0
    while i < len(l):
        if l[i] in ['e', 'w']:
            d.append(l[i])
            i += 1
        else:
            d.append(l[i:i + 2])
            i += 2
    lines.append(d)

#print(lines)

#n = 200
#tiles = np.zeros((n, n))
#for l in lines:
#    pos = (n // 2, n // 2)
#    for d in l:
#        pos = tuple(map(operator.add, pos, dirs[d]))
#    #print(pos)
#    tiles[pos] = int(tiles[pos]) ^ 1
#
#count = 0
#for t in tiles:
#    for a in t:
#        if a % 2 == 1:
#            count += 1
#print(count)

#days = 100
#for i in range(days):
#    new = np.copy(tiles)
#    count = 0
#    for t in tiles:
#        for a in t:
#            if a % 2 == 1:
#                count += 1
#    #print(i, count)
#
#    for x in range(n):
#        for y in range(n):
#            adj = 0
#            for d in dirs.values():
#                pos = tuple(map(operator.add, (x, y), d))
#                if any([x < 0 or x >= n for x in pos]):
#                    continue
#                if tiles[pos] == 1:
#                    adj += 1
#            cur = tiles[(x, y)]
#            if cur == 1 and (adj == 0 or adj > 2):
#                new[(x, y)] = 0
#            elif cur == 0 and adj == 2:
#                new[(x, y)] = 1
#
#    tiles = new
#count = 0
#for t in tiles:
#    for a in t:
#        if a % 2 == 1:
#            count += 1
#print(count)

tiles = {}
for l in lines:
    pos = 0
    for dir in l:
        pos += dirs[dir]
    #print(pos)
    if pos in tiles:
        del tiles[pos]
    else:
        tiles[pos] = True

count = 0
for t in tiles.values():
    count += t
print(count)

days = 100
for i in range(days):
    new = tiles.copy()
    count = 0
    for t in tiles.values():
        count += t
    #print(i, count)

    xs = [int(x.real) for x in tiles.keys()]
    ys = [int(x.imag) for x in tiles.keys()]
    for x in range(min(xs) - 1, max(xs) + 2):
        for y in range(min(ys) - 1, max(ys) + 2):
            p = x + y * 1j
            adj = 0
            for d in dirs.values():
                if p + d in tiles:
                    adj += 1
            if p in tiles and (adj == 0 or adj > 2):
                del new[p]
            elif p not in tiles and adj == 2:
                new[p] = True

    tiles = new.copy()

count = 0
for t in tiles.values():
    count += t
print(count)
