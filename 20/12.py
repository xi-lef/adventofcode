import sys

lines = []
for l in sys.stdin:
    l = l.rstrip('\n')
    lines.append((l[0], int(l[1:])))

dirs = ['E', 'N', 'W', 'S']
dir = 0
x = y = 0

for p in lines:
    d, v = p
    if d == 'F':
        d = dirs[dir % len(dirs)]

    if d == 'N':
        y += v
    elif d == 'E':
        x += v
    elif d == 'S':
        y -= v
    elif d == 'W':
        x -= v
    elif d == 'R':
        dir = int(dir - v / 90)
    elif d == 'L':
        dir = int(dir + v / 90)

print(f'manhattan distance: {abs(x) + abs(y)}')

dir = 0
x = y = 0
wp_x = 10
wp_y = 1

for p in lines:
    d, v = p
    if d == 'F':
        x += v * wp_x
        y += v * wp_y
    elif d == 'N':
        wp_y += v
    elif d == 'E':
        wp_x += v
    elif d == 'S':
        wp_y -= v
    elif d == 'W':
        wp_x -= v
    elif d in ['R', 'L']:
        v //= 90
        if d == 'R':
            d = 'L'
            v = 4 - v
        old = dir
        dir = (dir + v) % len(dirs)
        #for _ in range(v):
        #    wp_x, wp_y = -wp_y, wp_x
        if v == 1:
            wp_x, wp_y = -wp_y, wp_x
        elif v == 2:
            wp_x, wp_y = -wp_x, -wp_y
        else:
            wp_x, wp_y = wp_y, -wp_x

print(f'correct manhattan distance: {abs(x) + abs(y)}')
