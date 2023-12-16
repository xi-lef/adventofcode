def turn(lines):
    return list(''.join(z) for z in zip(*lines))

lines = [l.strip() for l in open(0)]
i = 0
galaxies = {}
for y, l in enumerate(lines):
    for x, c in enumerate(l):
        if c == '#':
            galaxies[i] = x + y * 1j
            i += 1

def solve(inc):
    new = galaxies.copy()
    for y, l in enumerate(lines):
        if '#' not in l:
            for galaxy, pos in galaxies.items():
                if pos.imag > y:
                    new[galaxy] += inc * 1j
    for x, l in enumerate(turn(lines)):
        if '#' not in l:
            for galaxy, pos in galaxies.items():
                if pos.real > x:
                    new[galaxy] += inc
    ret = 0
    for a in new.values():
        for b in new.values():
            ret += abs(a.real - b.real) + abs(a.imag - b.imag)
    return int(ret) // 2

print(solve(1))
print(solve(999999))
