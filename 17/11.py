import sys

moves = [m for m in sys.stdin.readline().strip().split(',')]

dirs = {'n':  1j, 'se': -1, 'sw':  1 - 1j,
        's': -1j, 'nw':  1, 'ne': -1 + 1j}

imax = lambda x: max(abs(x.real), abs(x.imag))
pos = furthest = 0
for m in moves:
    pos += dirs[m]
    furthest = max(furthest, pos, key = imax)
print(*(int(imax(x)) for x in (pos, furthest)))
