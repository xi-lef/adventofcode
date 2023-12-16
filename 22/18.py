import re

scan = set()
for l in open(0):
    scan.add(tuple(int(x) for x in re.findall(r'\d+', l)))

minx = min(x for x, _, _ in scan)
maxx = max(x for x, _, _ in scan)
miny = min(y for _, y, _ in scan)
maxy = max(y for _, y, _ in scan)
minz = min(z for _, _, z in scan)
maxz = max(z for _, _, z in scan)
dirs = ((-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1))

inside_cubes = set()
def inside(x, y, z):
    visited = set()
    stack = [(x, y, z)]
    while stack:
        cur = x, y, z = stack.pop()
        if cur in visited:
            continue
        visited.add(cur)

        if (x not in range(minx, maxx + 1)
                or y not in range(miny, maxy + 1)
                or z not in range(minz, maxz + 1)):
            return False

        for dx, dy, dz in dirs:
            next = (x + dx, y + dy, z + dz)
            if next in inside_cubes: return True
            elif next not in scan: stack.append(next)

    inside_cubes.update(visited, stack)
    return True

sum1 = sum2 = 0
for x, y, z in scan:
    for dx, dy, dz in dirs:
        new = (x + dx, y + dy, z + dz)
        if new not in scan:
            sum1 += 1
            if not inside(*new):
                sum2 += 1

print(sum1)
print(sum2)
