import sys
from collections import Counter

UP, RIGHT, DOWN, LEFT, DEAD = -1j, 1, 1j, -1, 69
dirs = {UP: -1j, RIGHT: 1, DOWN: 1j, LEFT: -1}

map = {}
carts = []
for y, l in enumerate(sys.stdin):
    l = l.strip('\n')
    for x, c in enumerate(l):
        val = x + y * 1j
        if c in '^>v<':
            dir = {'^': UP, '>': RIGHT, 'v': DOWN, '<': LEFT}[c]
            carts.append((val, dir, 0))
            c = '-' if c in '<>' else '|'
        map[val] = c

first = True
while True:
    carts = [c for c in carts if c[1] != DEAD]
    if len(carts) == 1:
        v = carts[0][0]
        print(f'{int(v.real)},{int(v.imag)}')
        break
    carts.sort(key = lambda t: (t[0].imag, t[0].real))

    for i, (val, d, t) in enumerate(carts):
        if d == DEAD:
            continue

        p = map[val]
        if p == '+':
            if t == 0:
                d *= -1j
            elif t == 1:
                pass
            else:
                d *= 1j
            t = (t + 1) % 3
        elif p == '\\':
            d *= -1j if d.real == 0 else 1j
        elif p == '/':
            d *= 1j if d.real == 0 else -1j

        val += dirs[d]
        carts[i] = (val, d, t)

        crashes = [c for c, n in Counter([t[0] for t in carts]).items() if n == 2]
        for crash in crashes:
            if first:
                first = False
                print(f'{int(val.real)},{int(val.imag)}')
            for i, c in enumerate(carts):
                if c[0] == crash:
                    carts[i] = (carts[i][0], DEAD, carts[i][2])
