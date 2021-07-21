import math
import sys
from itertools import count

earliest = int(sys.stdin.readline())
all = [t if t == 'x' else int(t) for t in sys.stdin.readline().split(',')]
ids = [int(x) for x in all if x != 'x']

m = math.inf
bus = 0
for id in ids:
    cur = (earliest // id + 1) * id
    if cur < m:
        m = cur
        bus = id

print(f'product is {bus * (m - earliest)}')

cur = 100000000000000
step = 1
for num, t in enumerate(all):
    if isinstance(t, str):
        continue
    cur = next(i for i in count(cur, step) if (i + num) % t == 0)
    #for i in itertools.count(cur, step):
    #    if (i + num) % t == 0:
    #        cur = i
    #        break
    step *= t
print(cur)
