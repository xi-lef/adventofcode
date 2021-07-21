import sys
from collections import deque
from itertools import permutations

lines = sys.stdin.readlines()

def scramble(pw):
    pw = deque(pw)
    for l in lines:
        op, *r = l.split()
        x, y = r[1], r[-1]
        if op == 'swap':
            if r[0] == 'position':
                f = int
            else:
                f = lambda a: pw.index(a)
            x, y = map(f, (x, y))
            pw[x], pw[y] = pw[y], pw[x]
        elif op == 'rotate':
            if r[0] == 'based':
                i = pw.index(y)
                num = 1 + i + (i >= 4)
            else:
                num = (1 if r[0] == 'right' else -1) * int(x)
            pw.rotate(num)
        elif op == 'reverse':
            x, y = map(int, (x, y))
            lpw = list(pw)
            pw = deque(lpw[: x] + lpw[x : y + 1][:: -1] + lpw[y + 1 :])
        elif op == 'move':
            x, y = map(int, (x, y))
            c = pw[x]
            del pw[x]
            pw.insert(y, c)
    return ''.join(pw)

start = 'abcdefgh'
print(scramble(start))
for p in permutations(start):
    if scramble(p) == 'fbgdceah':
        print(''.join(p))
        break
