from collections import defaultdict
import sys

# #1 @ 12,548: 19x10
claims = {}
for line in sys.stdin:
    id, r = line.strip()[1:].split(' @ ')
    start, size = r.split(': ')
    a, b = [int(x) for x in start.split(',')]
    w, h = [int(x) for x in size.split('x')]
    claims[int(id)] = (a, a + w, b, b + h)

#print(claims)

claimed = defaultdict(list)
for id, v in claims.items():
    for i in range(v[0], v[1]):
        for j in range(v[2], v[3]):
            claimed[(i, j)].append(id)

#print(claimed)
print(len([pos for pos, num in claimed.items() if len(num) > 1]))

for id, v in claims.items():
    good = True
    for i in range(v[0], v[1]):
        for j in range(v[2], v[3]):
            if len(claimed[(i, j)]) > 1:
                good = False
    if good:
        print(id)
        break
