from collections import Counter

poly, rules = open(0).read().split('\n\n')
last = poly[-1]
poly = Counter(poly[i : i + 2] for i in range(len(poly) - 1))
rules = dict(l.split(' -> ') for l in rules.strip().split('\n'))

for steps in (10, 40):
    pairs = poly
    for _ in range(steps):
        npairs = Counter()
        for (a, b), n in pairs.items():
            r = rules[a + b]
            npairs[a + r] += n
            npairs[r + b] += n
        pairs = npairs

    c = Counter()
    for (a, _), n in pairs.items():
        c[a] += n
    c[last] += 1  # last element is ignored by for-loop
    mc = c.most_common()
    print(mc[0][1] - mc[-1][1])
