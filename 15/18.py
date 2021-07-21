import sys

input = set()
for y, l in enumerate(sys.stdin):
    for x, c in enumerate(l):
        if c == '#':
            input.add(x + y * 1j)

for start in (set(), set([0, 99, 99j, 99 + 99j])):
    lights = input | start
    for _ in range(100):
        next = start.copy()
        for x in range(100):
            for y in range(100):
                c = 0
                for dx in (-1, 0, 1):
                    for dy in (-1, 0, 1):
                        if dx == dy == 0:
                            continue
                        c += x + dx + (y + dy) * 1j in lights
                p = x + y * 1j
                on = p in lights
                if on and c in (2, 3):
                    next.add(p)
                elif not on and c == 3:
                    next.add(p)
        lights = next
    print(len(lights))
