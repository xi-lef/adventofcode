lines = [l.strip() for l in open(0)]
W = len(lines)
H = len(lines[0])

cubes = set()
rocks = set()
for y, l in enumerate(lines):
    for x, c in enumerate(l):
        p = x + y * 1j
        if c == '#': cubes.add(p)
        elif c == 'O': rocks.add(p)

def tilt(rocks, dir):
    rocks = sorted(rocks, key = lambda i: i.imag if dir.imag else i.real,
                   reverse = dir.real > 0 or dir.imag > 0)
    tilted_rocks = set()
    for rock in rocks:
        for _ in range(W):
            nrock = rock + dir
            if (nrock in cubes or nrock in tilted_rocks
                    or not 0 <= nrock.real < H
                    or not 0 <= nrock.imag < W):
                break
            rock = nrock
        tilted_rocks.add(rock)
    return tilted_rocks

def score(rocks):
    return int(sum(H - r.imag for r in rocks))

def pr(rocks):
    for y in range(H):
        for x in range(W):
            p = x + y * 1j
            if p in cubes: c = '#'
            elif p in rocks: c = 'O'
            else: c = '.'
            print(c, end = '')
        print()

print(score(tilt(rocks, -1j)))

cycles = 1000000000
seen = []
cycle = 0
skip = False
while cycle < cycles:
    rocks = tilt(tilt(tilt(tilt(rocks, -1j), -1), 1j), 1)
    if not skip:
        t = tuple(rocks)
        if t in seen:
            cycle_len = len(seen) - seen.index(t) + 0
            cycle += (cycles - len(seen)) // cycle_len * cycle_len
            skip = True
        seen.append(t)

    cycle += 1
print(score(rocks))
