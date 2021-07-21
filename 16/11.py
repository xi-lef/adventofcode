import sys
from collections import defaultdict

gens = defaultdict(list)
chips = defaultdict(list)
for floor, l in enumerate(sys.stdin, start = 1):
    l = l.strip()[:-1].split()[4:]
    if l[0] == 'nothing':
        continue
    i = 0
    while i < len(l):
        if l[i] == 'and':
            i += 1
        if l[i + 2].strip(',') == 'generator':
            gens[floor].append(l[i + 1])
        else:
            chips[floor].append(l[i + 1].split('-')[0])
        i += 3
print(gens)
print(chips)

visited = set()

def bla(gens, chips, steps):
    if len(gens) == 1 and 4 in gens and len(chips) == 1 and 4 in chips:
        return steps

    state = tuple((k, tuple(v)) for d in (gens, chips) for k, v in sorted(d.items()))
    #print(state)
    if state in visited:
        return -1
    visited.add(state)

bla(gens, chips, 0)

#print(sum(2 * sum([8,2,0,0][:x]) - 3 for x in range(1,4)))
#print(sum(2 * sum([12,2,0,0][:x]) - 3 for x in range(1,4)))
