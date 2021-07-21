import sys

l = sys.stdin.readline().strip().split(', ')

d = p = 0
first = True
x = set()
for i in l:
    c, v = i[0], int(i[1:])
    d = (d + (1 if c == 'R' else -1)) % 4

    for _ in range(v):
        p += (-1 if d >= 2 else 1) * (1j if d % 2 == 1 else 1)
        if p in x and first:
            print('part 2:', abs(p.real) + abs(p.imag))
            first = False
        x.add(p)

print(abs(p.real) + abs(p.imag))
