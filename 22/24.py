from collections import defaultdict
from functools import cache

lines = [l.strip() for l in open(0).readlines()]

max_x = len(lines[0]) - 1
max_y = len(lines) - 1
start = lines[0].index('.')
end = lines[-1].index('.') + 1j * max_y

blizzards = {}
free = set()
for y, l in enumerate(lines):
    for x, c in enumerate(l):
        p = x + 1j * y
        if c != '#': free.add(p)
        if c in '><v^': blizzards[p] = c

@cache
def calc(minute):
    if minute == 0:
        global blizzards
        return blizzards

    prev = calc(minute - 1)
    new = defaultdict(str)
    for pos_, dirs in prev.items():
        for dir in dirs:
            pos = pos_
            pos += {'>': 1, '<': -1, 'v': 1j, '^': -1j}[dir]
            if pos.real == max_x: pos = complex(1, pos.imag)
            if pos.real == 0: pos = complex(max_x - 1, pos.imag)
            if pos.imag == max_y: pos = complex(pos.real, 1)
            if pos.imag == 0: pos = complex(pos.real, max_y - 1)
            new[pos] += dir

    return new

def pr(bs):
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            p = x + 1j * y
            if p in bs:
                val = bs[p]
                print(val if len(val) == 1 else len(val), end = '')
            elif p in free: print('.', end = '')
            else: print('#', end = '')
        print()

def bfs(start, end, starttime):
    stack = [(start, starttime)]
    visited = defaultdict(set)
    while stack:
        pos, min = stack.pop(0)
        if min in visited[pos]:
            continue
        visited[pos].add(min)

        if pos == end:
            return min

        blizz = calc(min + 1)
        for dir in (1, -1, 1j, -1j, 0):
            n = pos + dir
            if n in free and n not in blizz:
                stack.append((n, min + 1))

trip1 = bfs(start, end, 0)
print(trip1)
trip2 = bfs(end, start, trip1)
trip3 = bfs(start, end, trip2)
print(trip3)
