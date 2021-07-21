import sys

lines = [l.split() for l in sys.stdin]
reindeers = [tuple(map(int, (l[3], l[6], l[-2]))) for l in lines]
time = 2503

#dists = [(time // (r[1] + r[2]) * r[1] + min(r[1], time % (r[1] + r[2]))) * r[0]  for r in reindeers]
#print(max(dists))

cur = [0 for _ in reindeers]
points = cur[:]
for t in range(time):
    for i, r in enumerate(reindeers):
        if t % (r[1] + r[2]) < r[1]:
            cur[i] += r[0]
    m = max(cur)
    for i in range(len(points)):
        if cur[i] == m:
            points[i] += 1

print(max(cur), max(points))
