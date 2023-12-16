def draw():
    r = [x.real for x in rope]
    i = [x.imag for x in rope]
    minx = int(min(r)) - 10
    maxx = int(max(r)) + 10
    miny = int(min(i)) - 10
    maxy = int(max(i)) + 10
    for y in range(miny, maxy + 1):
        for x in range(minx, maxx + 1):
            if x == y == 0:
                print('s', end = '')
            elif x + 1j * y in rope:
                print('#', end = '')
            else:
                print('.', end = '')
        print()
    print()

steps = [l.split() for l in open(0)]

for knots in (2, 10):
    rope = [0 for _ in range(knots)]
    visited = set([rope[-1]])
    for dir, num in steps:
        for _ in range(int(num)):
            rope[0] += {'L': -1, 'R': 1, 'U': -1j, 'D': 1j}[dir]
            for k in range(1, knots):
                dx = rope[k - 1].real - rope[k].real
                dy = rope[k - 1].imag - rope[k].imag
                if abs(dx) > 1 or abs(dy) > 1:
                    rope[k] += min(max(dx, -1), 1) + 1j * min(max(dy, -1), 1)
                #draw()
            visited.add(rope[-1])
    print(len(visited))
