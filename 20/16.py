import sys

rules = []
for l in sys.stdin:
    if l == '\n':
        break
    name, l = l.rstrip('\n').split(':')
    l = l.split('or')
    l = [int(x) for x in '-'.join(l).split('-')]
    rules.append([l, name])

sys.stdin.readline()
mine = [int(x) for x in sys.stdin.readline().rstrip('\n').split(',')]

sys.stdin.readline()
sys.stdin.readline()
nearby = []
for l in sys.stdin:
    l = [int(x) for x in l.rstrip('\n').split(',')]
    nearby.append(l)

valids = nearby[:]
error = 0
for t in nearby:
    for v in t:
        valid = False
        for r, _ in rules:
            if r[0] <= v <= r[1] or r[2] <= v <= r[3]:
                valid = True
        if not valid:
            error += v
            if t in valids:
                valids.remove(t)

print(f'error rate: {error}')

valid_fields = [set(range(len(rules))) for _ in range(len(rules))]
for t in valids:
    for j, v in enumerate(t):
        valid_rules = set()
        for i, r in enumerate(rules):
            r = r[0]
            if r[0] <= v <= r[1] or r[2] <= v <= r[3]:
                valid_rules.add(i)
        valid_fields[j].intersection_update(valid_rules)

#print(valid_fields)
while any([len(s) > 1 for s in valid_fields]):
    for i, s in enumerate(valid_fields):
        if len(s) == 1:
            for other in valid_fields[0:i] + valid_fields[i + 1:]:
                other.difference_update(s)
#print(valid_fields)

bla = 1
for i, v in enumerate(mine):
    if rules[valid_fields[i].pop()][1].startswith('departure'):
        bla *= v

print(f'product of departure fields: {bla}')
