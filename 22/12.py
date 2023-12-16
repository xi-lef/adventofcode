area = {}
S = E = 0

for y, l in enumerate(open(0)):
    for x, c in enumerate(l.strip()):
        p = x + 1j * y
        if c == 'S':
            S = p
            c = 'a'
        elif c == 'E':
            E = p
            c = 'z'
        area[p] = ord(c) - ord('a')

def bfs(part2 = False):
    visited = set()
    stack : list[tuple[complex, int]] = [(S, 0)]
    if part2:
        for k, v in area.items():
            if v == 0:
                stack.append((k, 0))

    while stack:
        cur, steps = stack.pop(0)
        if cur in visited:
            continue
        visited.add(cur)
        if cur == E:
            print(steps)
            break

        for d in (1, -1, 1j, -1j):
            next = cur + d
            if next in area and area[next] - area[cur] <= 1:
                stack.append((next, steps + 1))

bfs()
bfs(True)
