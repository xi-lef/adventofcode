import sys

scan = {}
for l in sys.stdin:
    x, b = [p[2:] for p in l.strip().split(', ')]
    x = int(x)
    f, t = map(int, b.split('..'))
    for y in range(f, t + 1):
        p = x + 1j * y if l[0] == 'x' else y + 1j * x
        scan[p] = '#'
source = 500
