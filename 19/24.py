import sys
from collections import defaultdict

space = {}
for y, l in enumerate(sys.stdin):
    for x, c in enumerate(l.strip()):
        space[x + y * 1j] = c == '#'

def pr(space):
    s = ''
    for i, v in enumerate(space.values()):
        s += {0: '.', 1: '#', -1: '?'}[v]
        if (i + 1) % 5 == 0:
            s += '\n'
    print(s, '\n')

def update(space, k):
    adj = sum(space.get(k + d, 0) for d in (1, -1, 1j, -1j))
    return (space[k] and adj == 1) or (not space[k] and adj in (1, 2))

def grow(space):
    seen = set()
    while True:
        frozen = frozenset(tuple(i) for i in space.items())
        if frozen in seen:
            return sum(2 ** i for i, k in enumerate(space) if space[k])
        seen.add(frozen)

        space = {k: update(space, k) for k in space}
print(grow(space))

empty = {k: 0 for k in space}
space[2 + 2j] = empty[2 + 2j] = -1
spaces = defaultdict(lambda: empty.copy())
spaces[0] = space

def update2(spaces, d, k):
    space = spaces[d]
    v = space[k]
    if v == -1:
        return -1

    adj = 0
    for dir in (1, -1, 1j, -1j):
        n = space.get(k + dir, None)
        if n in (0, 1):
            adj += n
        elif n == -1:
            spacen = spaces[d + 1]
            adj += sum(spacen[(dir * -4 if dir in (-1, -1j) else 0)
                              + i * (1 if dir.imag else 1j)] for i in range(5))
        else:  # n == 2
            spacen = spaces[d - 1]
            adj += spacen[2 + 2j + dir]

    return (v and adj == 1) or (not v and adj in (1, 2))

def grow2(spaces):
    for m in range(200):
        nspaces = spaces.copy()
        for v in range(m // 2 + 2):
            for d in (v, -v):
                nspaces[d] = {k: update2(spaces, d, k) for k in spaces[d]}
        spaces = nspaces

    #for d, space in spaces.items():
    #    print('depth', d)
    #    pr(space)
    return sum(v for space in spaces.values() for v in space.values() if v == 1)
print(grow2(spaces))
