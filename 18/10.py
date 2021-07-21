from itertools import count
import math
import matplotlib.pyplot as plt
import sys

lines = [l.strip() for l in sys.stdin]

points = []
for l in lines:
    p, v = l.split(' velocity=<')
    px, py = [int(x) for x in p[p.index('<') + 1:-1].split(',')]
    vx, vy = [int(x) for x in v[:-1].split(',')]
    points.append([px, py, vx, vy])
#print(points)

pdx = math.inf
for time in count():
    new = [p[:] for p in points]
    for p in new:
        p[0] += p[2]
        p[1] += p[3]

    xs = [p[0] for p in new]
    dx = max(xs) - min(xs)
    if dx > pdx:
        break

    pdx = dx
    points = new

print(time)
X = [p[0] for p in points]
Y = [-p[1] for p in points]
plt.scatter(X, Y)
plt.show()
