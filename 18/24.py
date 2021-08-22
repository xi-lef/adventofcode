import re
import sys
from copy import deepcopy
from dataclasses import dataclass
from itertools import count

@dataclass
class Group():
    name: str
    num: int
    units: int
    hp: int
    dmg: int
    int: int
    immune: set[str]
    weak: set[str]
    type: str

    def __hash__(self):
        #return hash(self.name) + hash(self.num)
        return self.int

    def __repr__(self):
        return f'{self.name} group {self.num} ({self.units})'

def parse(name):
    army = []
    for i, l in enumerate(sys.stdin, start = 1):
        l = l.strip()
        if not l:
            break

        cur = [int(x) for x in re.findall(r'\d+', l)]
        for w in ('immune', 'weak'):
            elems = set()
            if w in l:
                elems.update(re.split(r'[;)]', l.split(f'{w} to ')[1])[0].split(', '))
            cur.append(elems)
        cur.append(l.split()[-5])

        army.append(Group(name, i, *cur))
    return army

sys.stdin.readline()
system = parse('IS')
sys.stdin.readline()
infection = parse('INF')

def choose(group, enemy):
    for e in enemy:
        if group.type in e.weak:
            return e
    for e in enemy:
        if group.type not in e.immune:
            return e
    return None

def sim(boost = 0):
    IS = deepcopy(system)
    INF = deepcopy(infection)
    for g in IS:
        g.dmg += boost

    while IS and INF:
        for a in (IS, INF):
            a.sort(key = lambda g: (g.units * g.dmg, g.int), reverse = True)

        targets = {}
        for attacker, defender in ((IS, INF.copy()), (INF, IS.copy())):
            for g in attacker:
                t = choose(g, defender)
                if t:
                    targets[g] = t
                    defender.remove(t)
        if not targets:
            break

        all = IS + INF
        all.sort(key = lambda g: g.int, reverse = True)
        for g in all:
            if g not in targets:
                continue
            t = targets[g]

            factor = 2 if g.type in t.weak else 1
            dmg = g.units * g.dmg * factor
            t.units = max(0, t.units - dmg // t.hp)

        for a in (IS, INF):
            a[:] = (g for g in a if g.units > 0)
    return IS, INF

print(sum(g.units for a in sim() for g in a))

for i in count():
    IS, INF = sim(i)
    if IS and not INF:
        print(sum(g.units for g in IS))
        break
