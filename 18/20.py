import sys
from collections import defaultdict
from functools import cache

path = sys.stdin.readline().strip()[1 :]
dirs = {'N': 1j, 'S': -1j, 'E': 1, 'W': -1}
rooms = defaultdict(set)

@cache
def walk(path, pos = 0):
    end = path.find('(')
    init = path[: end]
    for c in init:
        rooms[pos].add(c)
        pos += dirs[c]

    if end == -1:
        return
    path = path[end + 1 :]

    i = start = 0
    poss = set()
    depth = 1
    while depth > 0:
        c = path[i]
        if c == '(':
            depth += 1
        elif c == ')':
            depth -= 1
        if c == '|' and depth == 1 or depth == 0:
            poss.add(path[start : i])
            start = i + 1
        i += 1
    rest = path[i :]

    for p in poss:
        walk(p + rest, pos)
walk(path)

far = set()
stack = [(0, 0)]
visited = set()
while stack:
    steps, cur = stack.pop(0)
    if steps >= 1000:
        far.add(cur)
    visited.add(cur)
    for d in rooms[cur]:
        next = cur + dirs[d]
        if next not in visited:
            stack.append((steps + 1, next))
print(steps, len(far))
