import sys

lines = [l.strip().split(' <-> ') for l in sys.stdin]

pipes = {}
for line in lines:
    l, r = line
    pipes[int(l)] = [int(x) for x in r.split(', ')]

groups = set()
for l in pipes:
    group = set()

    stack = {l}
    while stack:
        x = stack.pop()
        group.add(x)
        for u in pipes[x]:
            if u in group:
                continue
            stack.add(u)

    groups.add(frozenset(group))

print(len(next(g for g in groups if 0 in g)), len(groups))
