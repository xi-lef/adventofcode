import sys
from collections import defaultdict
from copy import deepcopy
from itertools import permutations

lines = [l.strip().split() for l in sys.stdin]

people = set()
map = defaultdict(dict)
for l in lines:
    v = int(l[3])
    if l[2] == 'lose':
        v *= -1
    people.add(l[0])
    map[l[0]][l[-1][:-1]] = v

map = {k: {l: map[l][k] + v for l, v in d.items()} for k, d in map.items()}

#def find_best(seating = []):
#    n = len(seating)
#    if n == len(people):
#        return sum([map[seating[i]][seating[(i + 1) % n]] for i in range(n)])
#
#    m = 0
#    for n in people - set(seating):
#        m = max(m, find_best(seating + [n]))
#    return m

def find_best():
    n = len(people)
    m = 0
    for p in permutations(people):
        m = max(m, sum([map[p[i]][p[(i + 1) % n]] for i in range(n)]))
    return m

print(find_best())

for p in people:
    map[p]['me'] = 0
map['me'] = {p: 0 for p in people}
people.add('me')

print(find_best())

# extra lol
#for p in list(people):
#    op = people.copy()
#    om = deepcopy(map)
#
#    people.remove(p)
#    del map[p]
#    for m in map.values():
#        del m[p]
#
#    print('without', p, find_best())
#
#    people = op
#    map = om
