from collections import Counter

p1 = Counter()
points = Counter()
for l in open(0):
    x1, y1, x2, y2 = (int(v) for p in l.split(' -> ') for v in p.split(','))
    if x1 == x2 or y1 == y2:
        if x2 < x1 or y2 < y1:
            x1, y1, x2, y2 = x2, y2, x1, y1
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                p = [1j * y + x]
                points.update(p)
                p1.update(p)
    else:
        if y2 < y1:
            x1, y1, x2, y2 = x2, y2, x1, y1
        for i in range(y2 - y1 + 1):
            points.update([1j * (y1 + i) + x1 + (i if x1 < x2 else -i)])

print(sum(v > 1 for v in p1.values()))
print(sum(v > 1 for v in points.values()))
