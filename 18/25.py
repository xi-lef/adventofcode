import sys

points = [tuple(map(int, l.split(','))) for l in sys.stdin]

def dist(a, b):
    return sum(abs(c - d) for c, d in zip(a, b))

consts = []
while points:
    p = points.pop()
    for c in consts:
        if any(dist(p, x) <= 3 for x in c):
            c.append(p)

            for other in consts:
                if other == c:
                    continue
                if any(dist(p, o) <= 3 for o in other):
                    c.extend(other)
                    consts.remove(other)
            break
    else:
        consts.append([p])

print(len(consts))
