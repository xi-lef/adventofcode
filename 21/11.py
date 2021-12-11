from itertools import count

m = {y * 1j + x: int(c) for y, l in enumerate(open(0))
                        for x, c in enumerate(l.strip())}

flashes = 0
for i in count(1):
    for k in m:
        m[k] += 1

    flashed = set()
    s = [k for k in m if m[k] > 9]
    while s:
        c = s.pop(0)
        if c in flashed:
            continue
        flashed.add(c)

        for dx in (0, 1, -1):
            for dy in (0, 1j, -1j):
                n = c + dx + dy
                if n not in m:
                    continue
                m[n] += 1
                if m[n] == 10:
                    s.append(n)

    flashes += len(flashed)
    for k in flashed:
        m[k] = 0

    if i == 100:
        print(flashes)
    if len(flashed) == len(m):
        print(i)
        break
