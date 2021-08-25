import re
import sys
from itertools import count

clay = set()
for l in sys.stdin:
    x, *y = map(int, re.findall(r'\d+', l))
    for i in range(y[0], y[1] + 1):
        clay.add(x + i * 1j if l[0] == 'x' else i + x * 1j)

ys = [int(s.imag) for s in clay]
min_y, max_y = min(ys), max(ys)
wet = set()
water = set()

def pr():
    if not wet:
        return
    xs = [int(s.real) for s in wet]
    ys = [int(s.imag) for s in wet]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    for y in range(min_y - 2, max_y + 3):
        for x in range(min_x - 2, max_x + 3):
            p = x + y * 1j
            if p in clay:
                c = '#'
            elif p in water:
                c = '~'
            elif p in wet:
                c = '|'
            else:
                c = '.'
            print(c, end = '', flush = False)
        print()
    print()

def sim(cur):
    solid = clay | water

    while cur in solid:
        cur -= 1j
    while cur + 1j not in solid:
        if cur.imag > max_y:
            return None
        wet.add(cur)
        cur += 1j

    overflow = set()
    layer = set()
    for dir in (-1, 1):
        for n in count():
            new = cur + dir * n
            if new in solid:
                break
            layer.add(new)
            if new + 1j not in solid:
                overflow.add(new)
                break
    wet.update(layer)

    if overflow:
        return overflow
    water.update(layer)
    return {cur}

stack = {500 + min_y * 1j}
while stack:
    #pr()
    ret = sim(stack.pop())
    if ret:
        stack.update(ret)
print(len(wet))
print(len(water))
