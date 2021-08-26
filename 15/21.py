import sys
from itertools import combinations
from math import ceil

weapons = '''Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0'''
armors = '''Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5'''
rings = '''Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3'''

b_hp, b_atk, b_def = [int(l.split(': ')[1]) for l in sys.stdin]
my_hp = 100

def parse(area):
    nums = [l.split()[-3 :] for l in area.splitlines()]
    return [tuple(map(int, n)) for n in nums]

weapons = parse(weapons)
armors = parse(armors)
rings = parse(rings)

combs = []
for weapon in weapons:
    for armor in (c for r in (0, 1) for c in combinations(armors, r)):
        for ring in (c for r in (0, 1, 2) for c in combinations(rings, r)):
            combs.append(tuple(map(sum, zip(weapon, *armor, *ring))))
combs.sort(key = lambda t: t[0])

def fight(a_hp, a_atk, a_def, b_hp, b_atk, b_def):
    a_turns = ceil(a_hp / max(1, b_atk - a_def))
    b_turns = ceil(b_hp / max(1, a_atk - b_def))
    return a_turns >= b_turns

for c in combs:
    if fight(my_hp, c[1], c[2], b_hp, b_atk, b_def):
        print(c[0])
        break

for c in combs[:: -1]:
    if not fight(my_hp, c[1], c[2], b_hp, b_atk, b_def):
        print(c[0])
        break
