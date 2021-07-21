import sys
from collections import defaultdict

favnum = int(sys.stdin.readline())

def is_open(pos):
    x, y = int(pos.real), int(pos.imag)
    return (bin(x * x + 3 * x + 2 * x * y + y + y * y + favnum).count('1') % 2 == 0
            and x >= 0 and y >= 0)

target = 31 + 39j
shortest = defaultdict(lambda: 1e10)

def walk(cur, visited):
    steps = len(visited)

    if shortest[cur] <= steps:
        return 1e10
    shortest[cur] = steps

    if cur == target:
        return steps

    m = 1e10
    for dir in (1, 1j, -1, -1j):
        new = cur + dir
        if is_open(new) and new not in visited:
            m = min(m, walk(new, visited | set([new])))

    return m

print(walk(1 + 1j, set()))
print(len([1 for v in shortest.values() if v <= 50]))
