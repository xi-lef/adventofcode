import sys

all_ings = set()
lines = []
for l in sys.stdin:
    l = l.rstrip('\n')
    ings, alls = l.split(' (contains ')

    ings = set(ings.split())
    all_ings |= ings
    lines.append({a: ings for a in alls[:-1].split(', ')})

#print(lines)

bad = {}
for l in lines:
    for k in l:
        if k not in bad:
            bad[k] = l[k].copy()
        else:
            bad[k] &= (l[k])
#print('bad', bad)

bad_ings = {v for b in bad.values() for v in b}
good_ings = all_ings - bad_ings
#print('good ingredients', good_ings)
print(sum([g in list(l.values())[0] for g in good_ings for l in lines]))

while any(len(v) > 1 for v in bad.values()):
    #print(bad)
    for k, v in bad.items():
        if len(v) == 1:
            for j in bad:
                if j != k:
                    bad[j] -= v

l = list(bad.items())
l.sort(key = lambda p: p[0])
print(','.join(next(iter(p[1])) for p in l))
