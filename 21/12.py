from collections import defaultdict

m = defaultdict(set)
for l in open(0):
    a, b = l.strip().split('-')
    m[a].add(b)
    m[b].add(a)

for part2 in (False, True):
    num = 0
    s = [('start', {'start'}, None)]
    while s:
        c, v, twice = s.pop()
        for p in m[c]:
            if p == 'end':
                num += 1
            elif p not in v:
                s.append((p, v | ({p} if p.islower() else set()), twice))
            elif part2 and not twice and p != 'start':
                s.append((p, v, p))
    print(num)
