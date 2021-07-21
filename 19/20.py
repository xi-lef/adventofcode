import sys
from collections import defaultdict

open = set()
letters = {}

for y, l in enumerate(sys.stdin):
    for x, c in enumerate(l.rstrip()):
        p = x + y * 1j
        if c == '.':
            open.add(p)
        elif c not in ' #':
            letters[p] = c

portals = defaultdict(set)
while letters:
    a = next(iter(letters))
    for dir in (1, -1, 1j, -1j):
        b = a + dir
        if b in letters:
            name = letters[a] + letters[b]
            if a.real > b.real or a.imag > b.imag:
                name = name[:: -1]

            c = 0
            for x in (a, b):
                for dir in (1, -1, 1j, -1j):
                    n = x + dir
                    if n in open:
                        c = n
                        break
            portals[name].add(c)

            del letters[a], letters[b]

start = next(iter(portals['AA']))
end = next(iter(portals['ZZ']))
bla = {}
for t in portals.values():
    if len(t) == 1:
        continue
    a, b = t
    bla[a] = b
    bla[b] = a

stack = [(start, 0)]
dists = {}
while stack:
    p, s = stack.pop(0)
    if p in dists:
        continue
    dists[p] = s
    if p == end:
        break

    if p in bla:
        stack.append((bla[p], s + 1))
    for dir in (1, -1, 1j, -1j):
        n = p + dir
        if n in open:
            stack.append((n, s + 1))
print(dists[end])

w = max(k.real for k in bla)
h = max(k.imag for k in bla)
def is_outer(p):
    return p.real in (2, w) or p.imag in (2, h)

stack = [(start, 0, 0)]
dists = {}
while stack:
    p, d, s = stack.pop(0)
    if d < 0:
        continue

    if (p, d) in dists:
        continue
    dists[p, d] = s
    if p == end and d == 0:
        break

    if p in bla:
        stack.append((bla[p], d - 1 if is_outer(p) else d + 1, s + 1))
    for dir in (1, -1, 1j, -1j):
        n = p + dir
        if n in open:
            stack.append((n, d, s + 1))
print(dists[end, 0])
