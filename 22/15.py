import re

#ROW_Y = 10
ROW_Y = 2000000
#MAX = 20
MAX = 4000000
sensors = {}
objects_in_row = set()

for line in open(0):
    sx, sy, bx, by = (int(x) for x in re.findall(r'-?\d+', line))
    s = sx + 1j * sy
    b = bx + 1j * by
    sensors[s] = b
    if sy == ROW_Y: objects_in_row.add(sx)
    if by == ROW_Y: objects_in_row.add(bx)

def dist(a, b):
    return abs(a.real - b.real) + abs(a.imag - b.imag)

total = set()
borders = []
for sensor, beacon in sensors.items():
    sx, sy = sensor.real, sensor.imag
    # part 1
    dist_beacon = dist(sensor, beacon)
    dist_row = dist(sensor, sx + 1j * ROW_Y)

    diff = int(dist_beacon - dist_row)
    if diff >= 0:
        total.update(range(int(sx) - diff, int(sx) + diff + 1))

    # part 2
    d = int(dist_beacon) + 1
    points = [sensor + d, sensor - d, sensor + 1j * d, sensor - 1j * d]
    borders.append((points[0], points[2]))
    borders.append((points[0], points[3]))
    borders.append((points[1], points[2]))
    borders.append((points[1], points[3]))

print(len(total - objects_in_row))

def binsearch(L, R, sensor, dist_beacon):
    while abs(L - R) > 2:
        Lx, Ly, Rx, Ry = L.real, L.imag, R.real, R.imag
        d = abs(Lx - Rx) // 2
        m = complex(Lx + d * (1 if Lx < Rx else -1),
                    Ly + d * (1 if Ly < Ry else -1))
        if dist(sensor, m) <= dist_beacon:
            L = m
        else:
            R = m
    return R

for border in borders:
    a, b = border
    for sensor, beacon in sensors.items():
        dist_beacon = dist(sensor, beacon)
        a_in, b_in = (dist(sensor, p) <= dist_beacon for p in (a, b))
        covered = a_in + b_in
        if covered == 0:
            continue
        elif covered == 2:
            break

        if a_in:
            a = binsearch(a, b, sensor, dist_beacon)
        elif b_in:
            b = binsearch(b, a, sensor, dist_beacon)
        if not (0 <= a.real <= MAX and 0 <= b.real <= MAX) \
                or not (0 <= a.imag <= MAX and 0 <= b.imag <= MAX):
            break
    else:
        if a == b:
            print(int(a.real * MAX + a.imag))
            break
