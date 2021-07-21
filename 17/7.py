from collections import Counter
import sys

lines = [l.split() for l in sys.stdin]

weights = {}
struct = {}
for l in lines:
    weights[l[0]] = int(l[1][1:-1])
    if len(l) > 2:
        struct[l[0]] = set([t.replace(',', '') for t in l[3:]])
bottom, = set(weights) - {t for ts in struct.values() for t in ts}
print(bottom)

sums = {t: weights[t] for t in set(weights.keys()) - set(struct.keys())}
stack = set(struct.keys())
while stack:
    t = stack.pop()
    s = struct[t]
    if any(x not in sums for x in s):
        stack.add(t)
        continue
    sums[t] = sum([sums[x] for x in s]) + weights[t]

bad = prev = bottom
while True:
    under = struct[bad]
    wu = [sums[u] for u in under]
    if len(set(wu)) == 1:
        break

    bad_weight = Counter(wu).most_common()[-1][0]

    prev = bad
    bad = next(u for u in under if sums[u] == bad_weight)

w = [sums[x] for x in struct[prev]]
print(weights[bad] - (max(w) - min(w)))
